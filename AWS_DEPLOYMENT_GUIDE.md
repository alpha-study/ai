# Alpha AI Chatbot - AWS Deployment Guide

Complete guide for deploying the Alpha AI Chatbot to Amazon Web Services (AWS).

---

## Table of Contents

1. [Architecture Overview](#architecture-overview)
2. [AWS Services Required](#aws-services-required)
3. [Prerequisites](#prerequisites)
4. [Step 1: AWS Account Setup](#step-1-aws-account-setup)
5. [Step 2: RDS Database Setup](#step-2-rds-database-setup)
6. [Step 3: ElastiCache (Redis) Setup](#step-3-elasticache-redis-setup)
7. [Step 4: S3 Bucket Setup](#step-4-s3-bucket-setup)
8. [Step 5: EC2 Instance Setup](#step-5-ec2-instance-setup)
9. [Step 6: Application Deployment](#step-6-application-deployment)
10. [Step 7: Nginx Configuration](#step-7-nginx-configuration)
11. [Step 8: SSL Certificate Setup](#step-8-ssl-certificate-setup)
12. [Step 9: Domain Configuration](#step-9-domain-configuration)
13. [Step 10: Monitoring & Logging](#step-10-monitoring--logging)
14. [Alternative: ECS Deployment](#alternative-ecs-deployment)
15. [Cost Optimization](#cost-optimization)
16. [Security Best Practices](#security-best-practices)
17. [Backup & Recovery](#backup--recovery)
18. [Troubleshooting](#troubleshooting)

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         AWS Cloud                            │
│                                                              │
│  ┌──────────────┐     ┌──────────────┐                     │
│  │   Route 53   │────▶│ Load Balancer│                     │
│  │    (DNS)     │     │  (Optional)  │                     │
│  └──────────────┘     └──────┬───────┘                     │
│                              │                              │
│                    ┌─────────▼───────────┐                 │
│                    │   EC2 Instance(s)   │                 │
│                    │                     │                 │
│                    │  ┌──────────────┐  │                 │
│                    │  │    Nginx     │  │                 │
│                    │  └──────┬───────┘  │                 │
│                    │  ┌──────▼───────┐  │                 │
│                    │  │   Gunicorn   │  │                 │
│                    │  │  (Django App)│  │                 │
│                    │  └──────────────┘  │                 │
│                    │  ┌──────────────┐  │                 │
│                    │  │Celery Worker │  │                 │
│                    │  └──────────────┘  │                 │
│                    │  ┌──────────────┐  │                 │
│                    │  │  Chroma DB   │  │                 │
│                    │  └──────────────┘  │                 │
│                    └─────────┬───────────┘                 │
│                              │                              │
│         ┌────────────────────┼────────────────────┐        │
│         │                    │                    │        │
│    ┌────▼─────┐      ┌───────▼──────┐      ┌────▼────┐   │
│    │RDS       │      │ElastiCache   │      │   S3    │   │
│    │PostgreSQL│      │(Redis)       │      │ Bucket  │   │
│    └──────────┘      └──────────────┘      └─────────┘   │
│                                                              │
└─────────────────────────────────────────────────────────────┘
                           │
                           ▼
                  ┌─────────────────┐
                  │   OpenAI API    │
                  │  (External)     │
                  └─────────────────┘
```

---

## AWS Services Required

| Service | Purpose | Estimated Monthly Cost |
|---------|---------|----------------------|
| **EC2** | Application hosting | $15-50 (t3.small to t3.medium) |
| **RDS** | PostgreSQL database | $15-30 (db.t3.micro) |
| **ElastiCache** | Redis for Celery | $15-25 (cache.t3.micro) |
| **S3** | File storage | $1-5 (based on usage) |
| **Route 53** | DNS management | $0.50/month + queries |
| **Certificate Manager** | SSL/TLS certificates | Free |
| **CloudWatch** | Monitoring & logs | $5-10 |
| **Elastic IP** | Static IP address | Free (when attached) |
| **Total** | | **~$50-125/month** |

---

## Prerequisites

### Local Requirements

1. **AWS CLI installed**
   ```bash
   # macOS
   brew install awscli
   
   # Linux
   curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
   unzip awscliv2.zip
   sudo ./aws/install
   
   # Windows
   # Download from https://aws.amazon.com/cli/
   ```

2. **AWS Account with billing enabled**
   - Sign up at https://aws.amazon.com/
   - Add payment method

3. **SSH Key Pair**
   ```bash
   # Generate SSH key if you don't have one
   ssh-keygen -t rsa -b 4096 -C "your_email@example.com" -f ~/.ssh/aws-alpha-key
   ```

4. **Domain Name (Optional but recommended)**
   - Purchase from Route 53, Namecheap, GoDaddy, etc.

---

## Step 1: AWS Account Setup

### 1.1 Configure AWS CLI

```bash
# Configure AWS credentials
aws configure

# Enter when prompted:
# AWS Access Key ID: YOUR_ACCESS_KEY
# AWS Secret Access Key: YOUR_SECRET_KEY
# Default region name: us-east-1 (or your preferred region)
# Default output format: json
```

### 1.2 Create IAM User for Deployment

```bash
# Create IAM user
aws iam create-user --user-name alpha-deploy-user

# Attach necessary policies
aws iam attach-user-policy --user-name alpha-deploy-user \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess

aws iam attach-user-policy --user-name alpha-deploy-user \
  --policy-arn arn:aws:iam::aws:policy/AmazonRDSFullAccess

aws iam attach-user-policy --user-name alpha-deploy-user \
  --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess

# Create access keys
aws iam create-access-key --user-name alpha-deploy-user
```

### 1.3 Create VPC and Security Groups

```bash
# Create VPC (or use default)
aws ec2 create-vpc --cidr-block 10.0.0.0/16 --tag-specifications 'ResourceType=vpc,Tags=[{Key=Name,Value=alpha-vpc}]'

# Create security group
aws ec2 create-security-group \
  --group-name alpha-sg \
  --description "Security group for Alpha AI Chatbot" \
  --vpc-id vpc-xxxxx  # Replace with your VPC ID

# Allow SSH
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp --port 22 --cidr 0.0.0.0/0

# Allow HTTP
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp --port 80 --cidr 0.0.0.0/0

# Allow HTTPS
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp --port 443 --cidr 0.0.0.0/0
```

---

## Step 2: RDS Database Setup

### 2.1 Create RDS PostgreSQL Instance

**Via AWS Console:**

1. Go to AWS RDS Console: https://console.aws.amazon.com/rds/
2. Click "Create database"
3. Choose:
   - Engine type: **PostgreSQL**
   - Version: **PostgreSQL 15.x**
   - Template: **Free tier** (for testing) or **Production**
   - DB instance identifier: `alpha-db`
   - Master username: `alphaadmin`
   - Master password: (create strong password)
   - DB instance class: `db.t3.micro` (or larger)
   - Storage: 20 GB SSD
   - VPC: Select your VPC
   - Public access: **No** (for security)
   - VPC security group: Create new (allow PostgreSQL port 5432)
4. Click "Create database"

**Via AWS CLI:**

```bash
aws rds create-db-instance \
  --db-instance-identifier alpha-db \
  --db-instance-class db.t3.micro \
  --engine postgres \
  --master-username alphaadmin \
  --master-user-password YourStrongPassword123! \
  --allocated-storage 20 \
  --vpc-security-group-ids sg-xxxxx \
  --db-subnet-group-name default \
  --backup-retention-period 7 \
  --preferred-backup-window "03:00-04:00" \
  --preferred-maintenance-window "sun:04:00-sun:05:00"
```

### 2.2 Configure Security Group for RDS

```bash
# Allow EC2 security group to access RDS
aws ec2 authorize-security-group-ingress \
  --group-id sg-rds-xxxxx \
  --protocol tcp \
  --port 5432 \
  --source-group sg-ec2-xxxxx
```

### 2.3 Wait for Database to be Available

```bash
# Check status
aws rds describe-db-instances \
  --db-instance-identifier alpha-db \
  --query 'DBInstances[0].DBInstanceStatus'

# Wait until status is "available"
```

### 2.4 Get Database Endpoint

```bash
aws rds describe-db-instances \
  --db-instance-identifier alpha-db \
  --query 'DBInstances[0].Endpoint.Address'

# Save this endpoint - you'll need it for Django configuration
# Example: alpha-db.xxxxx.us-east-1.rds.amazonaws.com
```

---

## Step 3: ElastiCache (Redis) Setup

### 3.1 Create Redis Cluster

**Via AWS Console:**

1. Go to ElastiCache Console: https://console.aws.amazon.com/elasticache/
2. Click "Create" → "Redis cluster"
3. Configure:
   - Cluster engine: **Redis**
   - Name: `alpha-redis`
   - Node type: `cache.t3.micro`
   - Number of replicas: 0 (for development)
   - Subnet group: Select your VPC subnets
   - Security groups: Create new (allow Redis port 6379)
4. Click "Create"

**Via AWS CLI:**

```bash
aws elasticache create-cache-cluster \
  --cache-cluster-id alpha-redis \
  --cache-node-type cache.t3.micro \
  --engine redis \
  --num-cache-nodes 1 \
  --cache-subnet-group-name default \
  --security-group-ids sg-xxxxx
```

### 3.2 Get Redis Endpoint

```bash
aws elasticache describe-cache-clusters \
  --cache-cluster-id alpha-redis \
  --show-cache-node-info \
  --query 'CacheClusters[0].CacheNodes[0].Endpoint.Address'

# Save this endpoint
# Example: alpha-redis.xxxxx.0001.use1.cache.amazonaws.com
```

---

## Step 4: S3 Bucket Setup

### 4.1 Create S3 Bucket

```bash
# Create bucket (bucket names must be globally unique)
aws s3 mb s3://alpha-chatbot-media-YOUR-UNIQUE-ID --region us-east-1

# Enable versioning
aws s3api put-bucket-versioning \
  --bucket alpha-chatbot-media-YOUR-UNIQUE-ID \
  --versioning-configuration Status=Enabled
```

### 4.2 Configure Bucket Policy

Create a file `s3-policy.json`:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "AllowEC2Access",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::YOUR-ACCOUNT-ID:role/alpha-ec2-role"
      },
      "Action": [
        "s3:GetObject",
        "s3:PutObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::alpha-chatbot-media-YOUR-UNIQUE-ID/*",
        "arn:aws:s3:::alpha-chatbot-media-YOUR-UNIQUE-ID"
      ]
    }
  ]
}
```

Apply policy:

```bash
aws s3api put-bucket-policy \
  --bucket alpha-chatbot-media-YOUR-UNIQUE-ID \
  --policy file://s3-policy.json
```

### 4.3 Configure CORS (if needed for frontend)

Create `cors-config.json`:

```json
{
  "CORSRules": [
    {
      "AllowedOrigins": ["https://yourdomain.com"],
      "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
      "AllowedHeaders": ["*"],
      "MaxAgeSeconds": 3000
    }
  ]
}
```

Apply CORS:

```bash
aws s3api put-bucket-cors \
  --bucket alpha-chatbot-media-YOUR-UNIQUE-ID \
  --cors-configuration file://cors-config.json
```

---

## Step 5: EC2 Instance Setup

### 5.1 Launch EC2 Instance

**Via AWS Console:**

1. Go to EC2 Console: https://console.aws.amazon.com/ec2/
2. Click "Launch Instance"
3. Configure:
   - Name: `alpha-app-server`
   - AMI: **Ubuntu Server 22.04 LTS**
   - Instance type: **t3.small** (or t3.medium for production)
   - Key pair: Select or create new
   - Network: Your VPC
   - Subnet: Public subnet
   - Auto-assign public IP: **Enable**
   - Security group: Select `alpha-sg` created earlier
   - Storage: 30 GB gp3
4. Click "Launch instance"

**Via AWS CLI:**

```bash
aws ec2 run-instances \
  --image-id ami-0c55b159cbfafe1f0 \
  --instance-type t3.small \
  --key-name aws-alpha-key \
  --security-group-ids sg-xxxxx \
  --subnet-id subnet-xxxxx \
  --associate-public-ip-address \
  --block-device-mappings '[{"DeviceName":"/dev/sda1","Ebs":{"VolumeSize":30,"VolumeType":"gp3"}}]' \
  --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=alpha-app-server}]'
```

### 5.2 Allocate and Associate Elastic IP

```bash
# Allocate Elastic IP
aws ec2 allocate-address --domain vpc

# Associate with instance
aws ec2 associate-address \
  --instance-id i-xxxxx \
  --allocation-id eipalloc-xxxxx
```

### 5.3 Connect to EC2 Instance

```bash
# Get public IP
aws ec2 describe-instances \
  --instance-ids i-xxxxx \
  --query 'Reservations[0].Instances[0].PublicIpAddress'

# SSH into instance
ssh -i ~/.ssh/aws-alpha-key.pem ubuntu@YOUR-ELASTIC-IP
```

---

## Step 6: Application Deployment

### 6.1 Update System and Install Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and dependencies
sudo apt install -y python3.11 python3.11-venv python3.11-dev python3-pip
sudo apt install -y postgresql-client redis-tools
sudo apt install -y nginx supervisor
sudo apt install -y git curl wget

# Install build tools
sudo apt install -y build-essential libpq-dev libssl-dev libffi-dev
```

### 6.2 Create Application User

```bash
# Create user for running application
sudo useradd -m -s /bin/bash alphaapp
sudo usermod -aG sudo alphaapp

# Switch to application user
sudo su - alphaapp
```

### 6.3 Clone or Upload Application

```bash
# Create application directory
mkdir -p /home/alphaapp/alpha
cd /home/alphaapp/alpha

# Option 1: Clone from Git
git clone https://github.com/your-repo/alpha-ai-chatbot.git .

# Option 2: Upload via SCP (from local machine)
# scp -i ~/.ssh/aws-alpha-key.pem -r /Users/maddyb_007/Documents/dev/rohit/* ubuntu@YOUR-IP:/home/ubuntu/alpha/
# Then move to alphaapp directory
```

### 6.4 Create Virtual Environment

```bash
# Create virtual environment
python3.11 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
pip install -r requirements.txt

# Install additional production packages
pip install gunicorn psycopg2-binary boto3 django-storages
```

### 6.5 Configure Production Environment

Create `/home/alphaapp/alpha/.env`:

```bash
# Django Settings
SECRET_KEY=your-production-secret-key-generate-new-one
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com,YOUR-ELASTIC-IP

# Database (RDS PostgreSQL)
DATABASE_ENGINE=django.db.backends.postgresql
DATABASE_NAME=alphadb
DATABASE_USER=alphaadmin
DATABASE_PASSWORD=YourStrongPassword123!
DATABASE_HOST=alpha-db.xxxxx.us-east-1.rds.amazonaws.com
DATABASE_PORT=5432

# Redis (ElastiCache)
CELERY_BROKER_URL=redis://alpha-redis.xxxxx.0001.use1.cache.amazonaws.com:6379/0
CELERY_RESULT_BACKEND=redis://alpha-redis.xxxxx.0001.use1.cache.amazonaws.com:6379/0

# AWS S3 Configuration
USE_S3=True
AWS_STORAGE_BUCKET_NAME=alpha-chatbot-media-YOUR-UNIQUE-ID
AWS_S3_REGION_NAME=us-east-1
AWS_DEFAULT_ACL=private

# OpenAI Configuration
OPENAI_API_KEY=sk-proj-your-openai-api-key-here
AI_CHAT_MODEL=gpt-4o-mini
AI_EMBEDDING_MODEL=text-embedding-3-small
AI_MAX_RESPONSE_TOKENS=512

# Chroma Vector Database
CHROMA_DB_PATH=/home/alphaapp/alpha/chroma_db

# Security
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
```

### 6.6 Update Django Settings for Production

Edit `alpha_project/settings.py`:

```python
# Add at the top
import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Database configuration
if os.getenv('DATABASE_ENGINE'):
    DATABASES = {
        'default': {
            'ENGINE': os.getenv('DATABASE_ENGINE'),
            'NAME': os.getenv('DATABASE_NAME'),
            'USER': os.getenv('DATABASE_USER'),
            'PASSWORD': os.getenv('DATABASE_PASSWORD'),
            'HOST': os.getenv('DATABASE_HOST'),
            'PORT': os.getenv('DATABASE_PORT', '5432'),
        }
    }

# AWS S3 Configuration
if os.getenv('USE_S3') == 'True':
    AWS_STORAGE_BUCKET_NAME = os.getenv('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME = os.getenv('AWS_S3_REGION_NAME')
    AWS_DEFAULT_ACL = 'private'
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
    AWS_S3_OBJECT_PARAMETERS = {'CacheControl': 'max-age=86400'}
    
    # S3 Static and Media settings
    STATIC_LOCATION = 'static'
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATIC_LOCATION}/'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
    
    MEDIA_LOCATION = 'media'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIA_LOCATION}/'
    DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# Security settings for production
if not DEBUG:
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
```

### 6.7 Run Database Migrations

```bash
# Activate virtual environment
source venv/bin/activate

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

### 6.8 Test Application

```bash
# Test Django
python manage.py check

# Test database connection
python manage.py dbshell
# Type \q to exit

# Test Gunicorn
gunicorn alpha_project.wsgi:application --bind 0.0.0.0:8000
# Press Ctrl+C to stop
```

---

## Step 7: Nginx Configuration

### 7.1 Create Nginx Configuration

Create `/etc/nginx/sites-available/alpha`:

```bash
sudo nano /etc/nginx/sites-available/alpha
```

Add configuration:

```nginx
upstream alpha_app {
    server unix:/home/alphaapp/alpha/gunicorn.sock fail_timeout=0;
}

server {
    listen 80;
    server_name yourdomain.com www.yourdomain.com;
    
    # Redirect HTTP to HTTPS
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name yourdomain.com www.yourdomain.com;
    
    # SSL certificates (will be configured with Let's Encrypt)
    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;
    
    # SSL configuration
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;
    
    client_max_body_size 50M;
    
    # Logging
    access_log /var/log/nginx/alpha_access.log;
    error_log /var/log/nginx/alpha_error.log;
    
    location /static/ {
        # If using S3, this won't be used
        alias /home/alphaapp/alpha/staticfiles/;
    }
    
    location /media/ {
        # If using S3, this won't be used
        alias /home/alphaapp/alpha/media/;
    }
    
    location / {
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $http_host;
        proxy_redirect off;
        
        if (!-f $request_filename) {
            proxy_pass http://alpha_app;
            break;
        }
    }
}
```

### 7.2 Enable Nginx Site

```bash
# Enable site
sudo ln -s /etc/nginx/sites-available/alpha /etc/nginx/sites-enabled/

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx
sudo systemctl enable nginx
```

---

## Step 8: SSL Certificate Setup

### 8.1 Install Certbot

```bash
# Install Certbot
sudo apt install -y certbot python3-certbot-nginx
```

### 8.2 Obtain SSL Certificate

```bash
# Get certificate for your domain
sudo certbot --nginx -d yourdomain.com -d www.yourdomain.com

# Follow prompts:
# - Enter email address
# - Agree to terms
# - Choose whether to redirect HTTP to HTTPS (Yes)
```

### 8.3 Setup Auto-Renewal

```bash
# Test renewal
sudo certbot renew --dry-run

# Certbot automatically sets up cron job for renewal
# Verify:
sudo systemctl status certbot.timer
```

---

## Step 9: Configure Application Services

### 9.1 Create Gunicorn Systemd Service

Create `/etc/systemd/system/gunicorn.service`:

```bash
sudo nano /etc/systemd/system/gunicorn.service
```

Add:

```ini
[Unit]
Description=gunicorn daemon for Alpha AI Chatbot
After=network.target

[Service]
User=alphaapp
Group=www-data
WorkingDirectory=/home/alphaapp/alpha
EnvironmentFile=/home/alphaapp/alpha/.env

ExecStart=/home/alphaapp/alpha/venv/bin/gunicorn \
    --workers 3 \
    --bind unix:/home/alphaapp/alpha/gunicorn.sock \
    --timeout 60 \
    --access-logfile /home/alphaapp/alpha/logs/gunicorn-access.log \
    --error-logfile /home/alphaapp/alpha/logs/gunicorn-error.log \
    alpha_project.wsgi:application

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 9.2 Create Celery Systemd Service

Create `/etc/systemd/system/celery.service`:

```bash
sudo nano /etc/systemd/system/celery.service
```

Add:

```ini
[Unit]
Description=Celery Worker for Alpha AI Chatbot
After=network.target

[Service]
Type=forking
User=alphaapp
Group=alphaapp
WorkingDirectory=/home/alphaapp/alpha
EnvironmentFile=/home/alphaapp/alpha/.env

ExecStart=/home/alphaapp/alpha/venv/bin/celery -A alpha_project worker \
    --loglevel=info \
    --logfile=/home/alphaapp/alpha/logs/celery.log \
    --pidfile=/home/alphaapp/alpha/celery.pid

Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

### 9.3 Create Log Directories

```bash
# Create log directories
sudo mkdir -p /home/alphaapp/alpha/logs
sudo chown -R alphaapp:alphaapp /home/alphaapp/alpha/logs
```

### 9.4 Start Services

```bash
# Reload systemd
sudo systemctl daemon-reload

# Enable and start Gunicorn
sudo systemctl enable gunicorn
sudo systemctl start gunicorn
sudo systemctl status gunicorn

# Enable and start Celery
sudo systemctl enable celery
sudo systemctl start celery
sudo systemctl status celery
```

---

## Step 10: Domain Configuration

### 10.1 Configure Route 53 (if using AWS DNS)

```bash
# Create hosted zone
aws route53 create-hosted-zone --name yourdomain.com --caller-reference $(date +%s)

# Get nameservers and update at your domain registrar

# Create A record pointing to Elastic IP
aws route53 change-resource-record-sets \
  --hosted-zone-id Z1234567890ABC \
  --change-batch '{
    "Changes": [{
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "yourdomain.com",
        "Type": "A",
        "TTL": 300,
        "ResourceRecords": [{"Value": "YOUR-ELASTIC-IP"}]
      }
    }]
  }'

# Create www CNAME
aws route53 change-resource-record-sets \
  --hosted-zone-id Z1234567890ABC \
  --change-batch '{
    "Changes": [{
      "Action": "CREATE",
      "ResourceRecordSet": {
        "Name": "www.yourdomain.com",
        "Type": "CNAME",
        "TTL": 300,
        "ResourceRecords": [{"Value": "yourdomain.com"}]
      }
    }]
  }'
```

### 10.2 Or Configure External DNS

If not using Route 53:
1. Go to your domain registrar
2. Add A record: `@` → `YOUR-ELASTIC-IP`
3. Add CNAME record: `www` → `yourdomain.com`
4. Wait for DNS propagation (up to 48 hours)

---

## Step 11: Monitoring & Logging

### 11.1 Configure CloudWatch

Install CloudWatch agent:

```bash
wget https://s3.amazonaws.com/amazoncloudwatch-agent/ubuntu/amd64/latest/amazon-cloudwatch-agent.deb
sudo dpkg -i -E ./amazon-cloudwatch-agent.deb

# Configure CloudWatch
sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-config-wizard
```

### 11.2 Setup Application Logging

Edit Django settings to log to files:

```python
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{levelname} {asctime} {module} {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': '/home/alphaapp/alpha/logs/django.log',
            'maxBytes': 1024*1024*10,  # 10MB
            'backupCount': 10,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
```

### 11.3 Setup Log Rotation

```bash
sudo nano /etc/logrotate.d/alpha
```

Add:

```conf
/home/alphaapp/alpha/logs/*.log {
    daily
    rotate 14
    compress
    delaycompress
    notifempty
    create 0644 alphaapp alphaapp
    sharedscripts
    postrotate
        systemctl reload gunicorn
        systemctl reload celery
    endscript
}
```

---

## Alternative: ECS Deployment

If you prefer containerized deployment using Amazon ECS:

### 1. Create Dockerfile

```dockerfile
FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Run Gunicorn
CMD ["gunicorn", "alpha_project.wsgi:application", "--bind", "0.0.0.0:8000"]
```

### 2. Push to ECR

```bash
# Create ECR repository
aws ecr create-repository --repository-name alpha-chatbot

# Login to ECR
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin YOUR-ACCOUNT-ID.dkr.ecr.us-east-1.amazonaws.com

# Build and push
docker build -t alpha-chatbot .
docker tag alpha-chatbot:latest YOUR-ACCOUNT-ID.dkr.ecr.us-east-1.amazonaws.com/alpha-chatbot:latest
docker push YOUR-ACCOUNT-ID.dkr.ecr.us-east-1.amazonaws.com/alpha-chatbot:latest
```

### 3. Create ECS Cluster and Task Definition

Use ECS Console or CLI to create cluster and deploy the container.

---

## Cost Optimization

### Tips to Reduce AWS Costs

1. **Use Reserved Instances** (save 30-70%)
   ```bash
   # Purchase 1-year reserved instance
   aws ec2 purchase-reserved-instances-offering --instance-type t3.small
   ```

2. **Use Spot Instances** for non-critical workloads (save up to 90%)

3. **Enable Auto-scaling** to scale down during low traffic

4. **Clean up unused resources**:
   ```bash
   # Delete old snapshots
   aws ec2 describe-snapshots --owner-ids self
   aws ec2 delete-snapshot --snapshot-id snap-xxxxx
   
   # Delete unused EBS volumes
   aws ec2 describe-volumes --filters Name=status,Values=available
   ```

5. **Use S3 Lifecycle Policies** to move old files to cheaper storage

6. **Monitor with Cost Explorer** and set billing alerts

---

## Security Best Practices

### 1. IAM Roles and Policies

Use least privilege principle:

```bash
# Create IAM role for EC2
aws iam create-role --role-name alpha-ec2-role --assume-role-policy-document file://trust-policy.json

# Attach minimal required policies
aws iam attach-role-policy --role-name alpha-ec2-role --policy-arn arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess
```

### 2. Security Group Rules

Restrict access:

```bash
# Only allow SSH from your IP
aws ec2 authorize-security-group-ingress \
  --group-id sg-xxxxx \
  --protocol tcp --port 22 --cidr YOUR-IP/32

# Use VPN or bastion host for SSH access
```

### 3. Enable AWS Shield and WAF

```bash
# Enable AWS Shield Standard (free)
# Protects against DDoS attacks

# Setup WAF for additional protection against SQL injection, XSS, etc.
```

### 4. Encrypt Data

- Enable encryption at rest for RDS
- Enable encryption for S3 buckets
- Use SSL/TLS for all connections

### 5. Regular Security Updates

```bash
# Setup unattended upgrades on Ubuntu
sudo apt install unattended-upgrades
sudo dpkg-reconfigure -plow unattended-upgrades
```

---

## Backup & Recovery

### 1. Database Backups

```bash
# Enable automated backups in RDS (already configured)
# Manual backup:
aws rds create-db-snapshot \
  --db-instance-identifier alpha-db \
  --db-snapshot-identifier alpha-db-backup-$(date +%Y%m%d)
```

### 2. Application Backups

```bash
# Backup Chroma database
cd /home/alphaapp/alpha
tar -czf chroma_backup_$(date +%Y%m%d).tar.gz chroma_db/

# Upload to S3
aws s3 cp chroma_backup_$(date +%Y%m%d).tar.gz s3://alpha-backups/
```

### 3. Automated Backup Script

Create `/home/alphaapp/backup.sh`:

```bash
#!/bin/bash
DATE=$(date +%Y%m%d)

# Backup Chroma
tar -czf /tmp/chroma_backup_$DATE.tar.gz /home/alphaapp/alpha/chroma_db/

# Upload to S3
aws s3 cp /tmp/chroma_backup_$DATE.tar.gz s3://alpha-backups/chroma/

# Clean up
rm /tmp/chroma_backup_$DATE.tar.gz

# Keep only last 30 days of backups
aws s3 ls s3://alpha-backups/chroma/ | head -n -30 | awk '{print $4}' | xargs -I {} aws s3 rm s3://alpha-backups/chroma/{}
```

Add to crontab:

```bash
# Run daily at 2 AM
0 2 * * * /home/alphaapp/backup.sh
```

---

## Troubleshooting

### Common Issues

#### 1. Gunicorn Not Starting

```bash
# Check logs
sudo journalctl -u gunicorn -f

# Test manually
sudo su - alphaapp
cd /home/alphaapp/alpha
source venv/bin/activate
gunicorn alpha_project.wsgi:application
```

#### 2. Database Connection Error

```bash
# Test database connection
psql -h alpha-db.xxxxx.rds.amazonaws.com -U alphaadmin -d alphadb

# Check security groups allow connection from EC2
```

#### 3. Redis Connection Error

```bash
# Test Redis connection
redis-cli -h alpha-redis.xxxxx.cache.amazonaws.com ping

# Check ElastiCache security groups
```

#### 4. Static Files Not Loading

```bash
# Collect static files
python manage.py collectstatic --noinput

# If using S3, verify AWS credentials:
aws s3 ls s3://alpha-chatbot-media-YOUR-UNIQUE-ID/
```

#### 5. 502 Bad Gateway

```bash
# Check Gunicorn socket
ls -la /home/alphaapp/alpha/gunicorn.sock

# Check Nginx error logs
sudo tail -f /var/log/nginx/alpha_error.log

# Restart services
sudo systemctl restart gunicorn nginx
```

---

## Post-Deployment Checklist

- [ ] All services running (Gunicorn, Celery, Nginx, Redis, PostgreSQL)
- [ ] SSL certificate installed and auto-renewal configured
- [ ] Domain pointing to correct IP
- [ ] Firewall and security groups configured
- [ ] Database backups enabled
- [ ] CloudWatch monitoring configured
- [ ] Application logging working
- [ ] Test document upload
- [ ] Test chat functionality
- [ ] Test JWT authentication
- [ ] Set up billing alerts
- [ ] Document deployed version and configuration

---

## Maintenance Commands

```bash
# Check service status
sudo systemctl status gunicorn celery nginx

# Restart services
sudo systemctl restart gunicorn celery nginx

# View logs
sudo journalctl -u gunicorn -f
sudo tail -f /home/alphaapp/alpha/logs/celery.log
sudo tail -f /var/log/nginx/alpha_error.log

# Update application
cd /home/alphaapp/alpha
git pull
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart gunicorn celery

# Clean up disk space
sudo apt autoremove
docker system prune -a  # if using Docker
```

---

## Support Resources

- **AWS Documentation**: https://docs.aws.amazon.com/
- **Django Deployment**: https://docs.djangoproject.com/en/stable/howto/deployment/
- **Gunicorn**: https://docs.gunicorn.org/
- **Nginx**: https://nginx.org/en/docs/
- **Certbot**: https://certbot.eff.org/

---

**Deployment Complete! 🚀**

Your Alpha AI Chatbot is now running on AWS with production-grade infrastructure!
