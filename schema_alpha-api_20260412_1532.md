# Database Schema — `alpha-api`

**Generated:** 2026-04-12 15:32  
**Host:** `194.164.148.150:3306`  
**Tables exported:** 116  

## Table of Contents

1. [`ai_chat_message`](#1-ai-chat-message)
2. [`ai_chat_session`](#2-ai-chat-session)
3. [`ai_document_chunk`](#3-ai-document-chunk)
4. [`ai_knowledge_document`](#4-ai-knowledge-document)
5. [`ai_mock_exam`](#5-ai-mock-exam)
6. [`ai_mock_exam_question`](#6-ai-mock-exam-question)
7. [`ai_research_query`](#7-ai-research-query)
8. [`assignment_questions`](#8-assignment-questions)
9. [`assignments`](#9-assignments)
10. [`auth_group`](#10-auth-group)
11. [`auth_group_permissions`](#11-auth-group-permissions)
12. [`auth_permission`](#12-auth-permission)
13. [`auth_user`](#13-auth-user)
14. [`auth_user_groups`](#14-auth-user-groups)
15. [`auth_user_user_permissions`](#15-auth-user-user-permissions)
16. [`book_categories`](#16-book-categories)
17. [`books`](#17-books)
18. [`canteen_facilities`](#18-canteen-facilities)
19. [`canteen_menus`](#19-canteen-menus)
20. [`canteen_teams`](#20-canteen-teams)
21. [`career_guidances`](#21-career-guidances)
22. [`career_guidances_meta_data`](#22-career-guidances-meta-data)
23. [`career_guidances_photos`](#23-career-guidances-photos)
24. [`career_guidances_videos`](#24-career-guidances-videos)
25. [`caste_categories`](#25-caste-categories)
26. [`classes`](#26-classes)
27. [`complaints`](#27-complaints)
28. [`culture_photos`](#28-culture-photos)
29. [`culture_sponsers`](#29-culture-sponsers)
30. [`culture_teams`](#30-culture-teams)
31. [`cultures`](#31-cultures)
32. [`dairies`](#32-dairies)
33. [`divisions`](#33-divisions)
34. [`django_admin_log`](#34-django-admin-log)
35. [`django_content_type`](#35-django-content-type)
36. [`django_migrations`](#36-django-migrations)
37. [`django_session`](#37-django-session)
38. [`education_loans`](#38-education-loans)
39. [`entrance_exam_meta_data`](#39-entrance-exam-meta-data)
40. [`entrance_exams`](#40-entrance-exams)
41. [`error_logs`](#41-error-logs)
42. [`exam_questions`](#42-exam-questions)
43. [`exam_types`](#43-exam-types)
44. [`exams`](#44-exams)
45. [`exhibition_photos`](#45-exhibition-photos)
46. [`exhibitions`](#46-exhibitions)
47. [`faculties`](#47-faculties)
48. [`institute_entrance_exams`](#48-institute-entrance-exams)
49. [`institute_facilities`](#49-institute-facilities)
50. [`institute_faculties`](#50-institute-faculties)
51. [`institute_fees`](#51-institute-fees)
52. [`institute_galleries`](#52-institute-galleries)
53. [`institute_leads`](#53-institute-leads)
54. [`institute_placed_students`](#54-institute-placed-students)
55. [`institute_placement_companies`](#55-institute-placement-companies)
56. [`institute_ratings`](#56-institute-ratings)
57. [`institute_stream_class_subject_teachers`](#57-institute-stream-class-subject-teachers)
58. [`institute_stream_classes`](#58-institute-stream-classes)
59. [`institute_streams`](#59-institute-streams)
60. [`institute_trip_photos`](#60-institute-trip-photos)
61. [`institute_trips`](#61-institute-trips)
62. [`institute_types`](#62-institute-types)
63. [`institutes`](#63-institutes)
64. [`lectures`](#64-lectures)
65. [`login_histories`](#65-login-histories)
66. [`message_deletions`](#66-message-deletions)
67. [`messages`](#67-messages)
68. [`mock_exam_faculties`](#68-mock-exam-faculties)
69. [`mock_exam_questions`](#69-mock-exam-questions)
70. [`mock_exam_streams`](#70-mock-exam-streams)
71. [`mock_exam_subject_faculties`](#71-mock-exam-subject-faculties)
72. [`mock_exam_subject_streams`](#72-mock-exam-subject-streams)
73. [`mock_exam_subjects`](#73-mock-exam-subjects)
74. [`mock_exams`](#74-mock-exams)
75. [`news_paper_categories`](#75-news-paper-categories)
76. [`news_papers`](#76-news-papers)
77. [`notifications`](#77-notifications)
78. [`opportunities`](#78-opportunities)
79. [`opportunity_candidates`](#79-opportunity-candidates)
80. [`post_comments`](#80-post-comments)
81. [`post_likes`](#81-post-likes)
82. [`post_photos`](#82-post-photos)
83. [`posts`](#83-posts)
84. [`question_options`](#84-question-options)
85. [`questions`](#85-questions)
86. [`report_cards`](#86-report-cards)
87. [`reports`](#87-reports)
88. [`sequelizemeta`](#88-sequelizemeta)
89. [`sport_accessories`](#89-sport-accessories)
90. [`sport_competitions`](#90-sport-competitions)
91. [`sport_teams`](#91-sport-teams)
92. [`states`](#92-states)
93. [`streams`](#93-streams)
94. [`student_assignment_question_answers`](#94-student-assignment-question-answers)
95. [`student_assignments`](#95-student-assignments)
96. [`student_attendances`](#96-student-attendances)
97. [`student_exam_question_answers`](#97-student-exam-question-answers)
98. [`student_exams`](#98-student-exams)
99. [`students`](#99-students)
100. [`subjects`](#100-subjects)
101. [`teachers`](#101-teachers)
102. [`timetables`](#102-timetables)
103. [`transport_details`](#103-transport-details)
104. [`transport_fees`](#104-transport-fees)
105. [`transport_teams`](#105-transport-teams)
106. [`user_block_users`](#106-user-block-users)
107. [`user_connections`](#107-user-connections)
108. [`user_favourite_institutes`](#108-user-favourite-institutes)
109. [`user_mock_exam_question_answers`](#109-user-mock-exam-question-answers)
110. [`user_mock_exams`](#110-user-mock-exams)
111. [`user_notification_settings`](#111-user-notification-settings)
112. [`user_privacy_settings`](#112-user-privacy-settings)
113. [`user_recent_books`](#113-user-recent-books)
114. [`user_save_books`](#114-user-save-books)
115. [`user_types`](#115-user-types)
116. [`users`](#116-users)

---

## 1. `ai_chat_message`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `role` | `varchar(16)` | NO | — | — | — |  |
| `message` | `longtext` | NO | — | — | — |  |
| `response` | `longtext` | YES | — | — | — |  |
| `tokens_used` | `int` | YES | — | — | — |  |
| `created_at` | `datetime(6)` | NO | — | — | — |  |
| `session_id` | `char(32)` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_chat_message_session_id_476520bc_fk_ai_chat_session_id` | — | BTREE | `session_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `ai_chat_message_session_id_476520bc_fk_ai_chat_session_id` | `session_id` | `ai_chat_session`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `ai_chat_message` (
  `id` char(32) NOT NULL,
  `role` varchar(16) NOT NULL,
  `message` longtext NOT NULL,
  `response` longtext,
  `tokens_used` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `session_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_chat_message_session_id_476520bc_fk_ai_chat_session_id` (`session_id`),
  CONSTRAINT `ai_chat_message_session_id_476520bc_fk_ai_chat_session_id` FOREIGN KEY (`session_id`) REFERENCES `ai_chat_session` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 2. `ai_chat_session`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `user_id` | `int` | YES | — | MUL | — |  |
| `created_at` | `datetime(6)` | NO | — | — | — |  |
| `updated_at` | `datetime(6)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_chat_session_user_id_5766f382` | — | BTREE | `user_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `ai_chat_session` (
  `id` char(32) NOT NULL,
  `user_id` int DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `updated_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_chat_session_user_id_5766f382` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 3. `ai_document_chunk`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `chunk_text` | `longtext` | NO | — | — | — |  |
| `embedding_vector` | `longblob` | YES | — | — | — |  |
| `vector_id` | `varchar(256)` | YES | — | — | — |  |
| `created_at` | `datetime(6)` | NO | — | — | — |  |
| `document_id` | `char(32)` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_document_chunk_document_id_b144efa0_fk_ai_knowle` | — | BTREE | `document_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `ai_document_chunk_document_id_b144efa0_fk_ai_knowle` | `document_id` | `ai_knowledge_document`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `ai_document_chunk` (
  `id` char(32) NOT NULL,
  `chunk_text` longtext NOT NULL,
  `embedding_vector` longblob,
  `vector_id` varchar(256) DEFAULT NULL,
  `created_at` datetime(6) NOT NULL,
  `document_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_document_chunk_document_id_b144efa0_fk_ai_knowle` (`document_id`),
  CONSTRAINT `ai_document_chunk_document_id_b144efa0_fk_ai_knowle` FOREIGN KEY (`document_id`) REFERENCES `ai_knowledge_document` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 4. `ai_knowledge_document`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `title` | `varchar(512)` | NO | — | — | — |  |
| `file` | `varchar(100)` | NO | — | — | — |  |
| `file_type` | `varchar(16)` | NO | — | — | — |  |
| `uploaded_by_id` | `int` | YES | — | MUL | — |  |
| `uploaded_at` | `datetime(6)` | NO | — | — | — |  |
| `processed` | `tinyint(1)` | NO | — | — | — |  |
| `metadata` | `json` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_knowledge_document_uploaded_by_id_bc14b592` | — | BTREE | `uploaded_by_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `ai_knowledge_document` (
  `id` char(32) NOT NULL,
  `title` varchar(512) NOT NULL,
  `file` varchar(100) NOT NULL,
  `file_type` varchar(16) NOT NULL,
  `uploaded_by_id` int DEFAULT NULL,
  `uploaded_at` datetime(6) NOT NULL,
  `processed` tinyint(1) NOT NULL,
  `metadata` json NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_knowledge_document_uploaded_by_id_bc14b592` (`uploaded_by_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 5. `ai_mock_exam`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `user_id` | `int` | YES | — | MUL | — |  |
| `subject` | `varchar(256)` | NO | — | — | — |  |
| `topic` | `varchar(512)` | NO | — | — | — |  |
| `difficulty` | `varchar(16)` | NO | — | — | — |  |
| `question_type` | `varchar(16)` | NO | — | — | — |  |
| `num_questions` | `int unsigned` | NO | — | — | — |  |
| `time_limit_minutes` | `int unsigned` | YES | — | — | — |  |
| `instructions` | `longtext` | NO | — | — | — |  |
| `tokens_used` | `int` | NO | — | — | — |  |
| `created_at` | `datetime(6)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_mock_exam_user_id_7179d7e6` | — | BTREE | `user_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `ai_mock_exam` (
  `id` char(32) NOT NULL,
  `user_id` int DEFAULT NULL,
  `subject` varchar(256) NOT NULL,
  `topic` varchar(512) NOT NULL,
  `difficulty` varchar(16) NOT NULL,
  `question_type` varchar(16) NOT NULL,
  `num_questions` int unsigned NOT NULL,
  `time_limit_minutes` int unsigned DEFAULT NULL,
  `instructions` longtext NOT NULL,
  `tokens_used` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_mock_exam_user_id_7179d7e6` (`user_id`),
  CONSTRAINT `ai_mock_exam_chk_1` CHECK ((`num_questions` >= 0)),
  CONSTRAINT `ai_mock_exam_chk_2` CHECK ((`time_limit_minutes` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 6. `ai_mock_exam_question`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `question_number` | `int unsigned` | NO | — | — | — |  |
| `question_type` | `varchar(16)` | NO | — | — | — |  |
| `question_text` | `longtext` | NO | — | — | — |  |
| `options` | `json` | NO | — | — | — |  |
| `correct_answer` | `longtext` | NO | — | — | — |  |
| `explanation` | `longtext` | NO | — | — | — |  |
| `marks` | `int unsigned` | NO | — | — | — |  |
| `exam_id` | `char(32)` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_mock_exam_question_exam_id_fd5885f3_fk_ai_mock_exam_id` | — | BTREE | `exam_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `ai_mock_exam_question_exam_id_fd5885f3_fk_ai_mock_exam_id` | `exam_id` | `ai_mock_exam`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `ai_mock_exam_question` (
  `id` char(32) NOT NULL,
  `question_number` int unsigned NOT NULL,
  `question_type` varchar(16) NOT NULL,
  `question_text` longtext NOT NULL,
  `options` json NOT NULL,
  `correct_answer` longtext NOT NULL,
  `explanation` longtext NOT NULL,
  `marks` int unsigned NOT NULL,
  `exam_id` char(32) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_mock_exam_question_exam_id_fd5885f3_fk_ai_mock_exam_id` (`exam_id`),
  CONSTRAINT `ai_mock_exam_question_exam_id_fd5885f3_fk_ai_mock_exam_id` FOREIGN KEY (`exam_id`) REFERENCES `ai_mock_exam` (`id`),
  CONSTRAINT `ai_mock_exam_question_chk_1` CHECK ((`question_number` >= 0)),
  CONSTRAINT `ai_mock_exam_question_chk_2` CHECK ((`marks` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 7. `ai_research_query`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `char(32)` | NO | — | PRI | — |  |
| `user_id` | `int` | YES | — | MUL | — |  |
| `topic` | `varchar(512)` | NO | — | — | — |  |
| `query` | `longtext` | NO | — | — | — |  |
| `response` | `longtext` | NO | — | — | — |  |
| `sources` | `json` | NO | — | — | — |  |
| `tokens_used` | `int` | NO | — | — | — |  |
| `created_at` | `datetime(6)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `ai_research_query_user_id_22b8dad2` | — | BTREE | `user_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `ai_research_query` (
  `id` char(32) NOT NULL,
  `user_id` int DEFAULT NULL,
  `topic` varchar(512) NOT NULL,
  `query` longtext NOT NULL,
  `response` longtext NOT NULL,
  `sources` json NOT NULL,
  `tokens_used` int NOT NULL,
  `created_at` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `ai_research_query_user_id_22b8dad2` (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 8. `assignment_questions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 1,016 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `assignmentId` | `int` | NO | — | — | — |  |
| `questionId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `assignment_questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `assignmentId` int NOT NULL,
  `questionId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1198 DEFAULT CHARSET=latin1
```

---

## 9. `assignments`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 187 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `examType` | `int` | NO | — | — | — | 1 - Objective/ 2 - Subjective |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteStreamClassId` | `int` | NO | — | — | — |  |
| `instituteStreamClassSubjectId` | `int` | NO | — | — | — |  |
| `startDate` | `date` | NO | — | — | — |  |
| `endDate` | `date` | NO | — | — | — |  |
| `totalMarks` | `int` | NO | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — | created by |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `assignments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `examType` int NOT NULL COMMENT '1 - Objective/ 2 - Subjective',
  `instituteId` int NOT NULL,
  `instituteStreamClassId` int NOT NULL,
  `instituteStreamClassSubjectId` int NOT NULL,
  `startDate` date NOT NULL,
  `endDate` date NOT NULL,
  `totalMarks` int NOT NULL,
  `teacherId` int NOT NULL COMMENT 'created by',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=203 DEFAULT CHARSET=latin1
```

---

## 10. `auth_group`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(150)` | NO | — | UNI | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `name` | ✅ | BTREE | `name` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `auth_group` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 11. `auth_group_permissions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `bigint` | NO | — | PRI | auto_increment |  |
| `group_id` | `int` | NO | — | MUL | — |  |
| `permission_id` | `int` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` | — | BTREE | `permission_id` |
| `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` | ✅ | BTREE | `group_id`, `permission_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` | `permission_id` | `auth_permission`.`id` | NO ACTION | NO ACTION |
| `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` | `group_id` | `auth_group`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 12. `auth_permission`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 56 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `content_type_id` | `int` | NO | — | MUL | — |  |
| `codename` | `varchar(100)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `auth_permission_content_type_id_codename_01ab375a_uniq` | ✅ | BTREE | `content_type_id`, `codename` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `auth_permission_content_type_id_2f476e4b_fk_django_co` | `content_type_id` | `django_content_type`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `auth_permission` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 13. `auth_user`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 1 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `password` | `varchar(128)` | NO | — | — | — |  |
| `last_login` | `datetime(6)` | YES | — | — | — |  |
| `is_superuser` | `tinyint(1)` | NO | — | — | — |  |
| `username` | `varchar(150)` | NO | — | UNI | — |  |
| `first_name` | `varchar(150)` | NO | — | — | — |  |
| `last_name` | `varchar(150)` | NO | — | — | — |  |
| `email` | `varchar(254)` | NO | — | — | — |  |
| `is_staff` | `tinyint(1)` | NO | — | — | — |  |
| `is_active` | `tinyint(1)` | NO | — | — | — |  |
| `date_joined` | `datetime(6)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |
| `username` | ✅ | BTREE | `username` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `auth_user` (
  `id` int NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 14. `auth_user_groups`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `bigint` | NO | — | PRI | auto_increment |  |
| `user_id` | `int` | NO | — | MUL | — |  |
| `group_id` | `int` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `auth_user_groups_group_id_97559544_fk_auth_group_id` | — | BTREE | `group_id` |
| `auth_user_groups_user_id_group_id_94350c0c_uniq` | ✅ | BTREE | `user_id`, `group_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `auth_user_groups_group_id_97559544_fk_auth_group_id` | `group_id` | `auth_group`.`id` | NO ACTION | NO ACTION |
| `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` | `user_id` | `auth_user`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 15. `auth_user_user_permissions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `bigint` | NO | — | PRI | auto_increment |  |
| `user_id` | `int` | NO | — | MUL | — |  |
| `permission_id` | `int` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` | — | BTREE | `permission_id` |
| `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` | ✅ | BTREE | `user_id`, `permission_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` | `permission_id` | `auth_permission`.`id` | NO ACTION | NO ACTION |
| `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` | `user_id` | `auth_user`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 16. `book_categories`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | YES | — | — | — |  |
| `keyName` | `varchar(255)` | YES | — | — | — |  |
| `name` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `book_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int DEFAULT NULL,
  `keyName` varchar(255) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1
```

---

## 17. `books`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 136 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `bookCategoryId` | `int` | NO | — | — | — |  |
| `facultyId` | `int` | YES | — | — | — |  |
| `streamId` | `int` | YES | — | — | — |  |
| `classId` | `int` | YES | — | — | — |  |
| `language` | `varchar(255)` | YES | — | — | — |  |
| `name` | `varchar(255)` | YES | — | — | — |  |
| `writerName` | `varchar(255)` | YES | — | — | — |  |
| `thumbnailUrl` | `varchar(255)` | YES | — | — | — |  |
| `bookUrl` | `varchar(255)` | YES | — | — | — |  |
| `pdfUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `bookCategoryId` int NOT NULL,
  `facultyId` int DEFAULT NULL,
  `streamId` int DEFAULT NULL,
  `classId` int DEFAULT NULL,
  `language` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `writerName` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `thumbnailUrl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `bookUrl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `pdfUrl` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=139 DEFAULT CHARSET=latin1
```

---

## 18. `canteen_facilities`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `facilities` | `text` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `canteen_facilities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `facilities` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1
```

---

## 19. `canteen_menus`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 9 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `itemType` | `smallint` | NO | — | — | — | 1 - snaks, 2 - meal |
| `itemName` | `varchar(255)` | NO | — | — | — |  |
| `itemAvtarUrl` | `varchar(255)` | YES | — | — | — |  |
| `price` | `double` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `canteen_menus` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `itemType` smallint NOT NULL COMMENT '1 - snaks, 2 - meal',
  `itemName` varchar(255) NOT NULL,
  `itemAvtarUrl` varchar(255) DEFAULT NULL,
  `price` double NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1
```

---

## 20. `canteen_teams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 5 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `position` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `canteen_teams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `userId` int NOT NULL,
  `position` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1
```

---

## 21. `career_guidances`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 45 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `facultyId` | `int` | NO | — | — | — |  |
| `streamId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `career_guidances` (
  `id` int NOT NULL AUTO_INCREMENT,
  `facultyId` int NOT NULL,
  `streamId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=51 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 22. `career_guidances_meta_data`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 185 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `careerGuidanceId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `career_guidances_meta_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `careerGuidanceId` int NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `desc` text COLLATE utf8mb4_general_ci,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=259 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 23. `career_guidances_photos`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 11 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `careerGuidanceId` | `int` | NO | — | — | — |  |
| `pathUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `career_guidances_photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `careerGuidanceId` int NOT NULL,
  `pathUrl` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 24. `career_guidances_videos`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `careerGuidanceId` | `int` | NO | — | — | — |  |
| `pathUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `career_guidances_videos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `careerGuidanceId` int NOT NULL,
  `pathUrl` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 25. `caste_categories`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `caste_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 26. `classes`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 5 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `className` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `classes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `className` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1
```

---

## 27. `complaints`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 32 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `status` | `int` | NO | 1 | — | — | 1 - Pending/2 - Resolved/ 3 - Reject |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `complaints` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `desc` text NOT NULL,
  `userId` int NOT NULL,
  `status` int NOT NULL DEFAULT '1' COMMENT '1 - Pending/2 - Resolved/ 3 - Reject',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1
```

---

## 28. `culture_photos`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 22 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `picUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `culture_photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `picUrl` varchar(255) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=26 DEFAULT CHARSET=latin1
```

---

## 29. `culture_sponsers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `varchar(255)` | NO | — | — | — |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `avtarUrl` | `varchar(255)` | YES | — | — | — |  |
| `mobile` | `varchar(255)` | YES | — | — | — |  |
| `amount` | `varchar(255)` | YES | — | — | — |  |
| `sponserFor` | `varchar(255)` | YES | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `culture_sponsers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `avtarUrl` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `amount` varchar(255) DEFAULT NULL,
  `sponserFor` varchar(255) DEFAULT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1
```

---

## 30. `culture_teams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — |  |
| `position` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `culture_teams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `teacherId` int NOT NULL,
  `position` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1
```

---

## 31. `cultures`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 5 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `cultureDate` | `date` | YES | — | — | — |  |
| `startTime` | `time` | YES | — | — | — |  |
| `endTime` | `time` | YES | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `cultures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `cultureDate` date DEFAULT NULL,
  `startTime` time DEFAULT NULL,
  `endTime` time DEFAULT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=latin1
```

---

## 32. `dairies`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 49 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `dairies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `title` varchar(255) NOT NULL,
  `desc` text CHARACTER SET latin1 COLLATE latin1_swedish_ci,
  `userId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=57 DEFAULT CHARSET=latin1
```

---

## 33. `divisions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 5 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `divisions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 34. `django_admin_log`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `action_time` | `datetime(6)` | NO | — | — | — |  |
| `object_id` | `longtext` | YES | — | — | — |  |
| `object_repr` | `varchar(200)` | NO | — | — | — |  |
| `action_flag` | `smallint unsigned` | NO | — | — | — |  |
| `change_message` | `longtext` | NO | — | — | — |  |
| `content_type_id` | `int` | YES | — | MUL | — |  |
| `user_id` | `int` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `django_admin_log_content_type_id_c4bce8eb_fk_django_co` | — | BTREE | `content_type_id` |
| `django_admin_log_user_id_c564eba6_fk_auth_user_id` | — | BTREE | `user_id` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

| Constraint | Column | References | On Update | On Delete |
|------------|--------|-----------|-----------|-----------|
| `django_admin_log_content_type_id_c4bce8eb_fk_django_co` | `content_type_id` | `django_content_type`.`id` | NO ACTION | NO ACTION |
| `django_admin_log_user_id_c564eba6_fk_auth_user_id` | `user_id` | `auth_user`.`id` | NO ACTION | NO ACTION |

### DDL

```sql
CREATE TABLE `django_admin_log` (
  `id` int NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `django_admin_log_chk_1` CHECK ((`action_flag` >= 0))
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 35. `django_content_type`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 14 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `app_label` | `varchar(100)` | NO | — | MUL | — |  |
| `model` | `varchar(100)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `django_content_type_app_label_model_76bd3d3b_uniq` | ✅ | BTREE | `app_label`, `model` |
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `django_content_type` (
  `id` int NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 36. `django_migrations`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 19 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `bigint` | NO | — | PRI | auto_increment |  |
| `app` | `varchar(255)` | NO | — | — | — |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `applied` | `datetime(6)` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 37. `django_session`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 1 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `session_key` | `varchar(40)` | NO | — | PRI | — |  |
| `session_data` | `longtext` | NO | — | — | — |  |
| `expire_date` | `datetime(6)` | NO | — | MUL | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `django_session_expire_date_a5c62663` | — | BTREE | `expire_date` |
| `PRIMARY` | ✅ | BTREE | `session_key` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 38. `education_loans`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 9 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `desc` | `text` | YES | — | — | — |  |
| `loanLinks` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `education_loans` (
  `id` int NOT NULL AUTO_INCREMENT,
  `desc` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `loanLinks` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1
```

---

## 39. `entrance_exam_meta_data`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 43 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `entranceExamId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `entrance_exam_meta_data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `entranceExamId` int NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `desc` text COLLATE utf8mb4_general_ci,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=46 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 40. `entrance_exams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 16 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `facultyId` | `int` | NO | — | — | — |  |
| `examName` | `varchar(255)` | NO | — | — | — |  |
| `examDesc` | `varchar(255)` | NO | — | — | — |  |
| `avtarUrl` | `varchar(255)` | YES | — | — | — |  |
| `status` | `smallint` | NO | 1 | — | — | 1 - Active/ 2 - Inactive |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `entrance_exams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `facultyId` int NOT NULL,
  `examName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `examDesc` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `avtarUrl` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `status` smallint NOT NULL DEFAULT '1' COMMENT '1 - Active/ 2 - Inactive',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 41. `error_logs`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 821 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `apiName` | `text` | YES | — | — | — |  |
| `method` | `varchar(200)` | YES | — | — | — |  |
| `userInfo` | `json` | YES | — | — | — |  |
| `requestPayload` | `json` | YES | — | — | — |  |
| `errorMessage` | `text` | YES | — | — | — |  |
| `errorStack` | `text` | YES | — | — | — |  |
| `status` | `smallint` | YES | 1 | — | — | 1 - Pending/2 - Resolve |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `error_logs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `apiName` text COLLATE utf8mb4_general_ci,
  `method` varchar(200) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `userInfo` json DEFAULT NULL,
  `requestPayload` json DEFAULT NULL,
  `errorMessage` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `errorStack` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `status` smallint DEFAULT '1' COMMENT '1 - Pending/2 - Resolve',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=883 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 42. `exam_questions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2,838 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `examId` | `int` | NO | — | — | — |  |
| `questionId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `exam_questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `examId` int NOT NULL,
  `questionId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3226 DEFAULT CHARSET=latin1
```

---

## 43. `exam_types`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 3 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `exam_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

---

## 44. `exams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 358 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `examTypeId` | `int` | NO | — | — | — |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteStreamClassId` | `int` | NO | — | — | — |  |
| `instituteStreamClassSubjectId` | `int` | NO | — | — | — |  |
| `examDate` | `date` | NO | — | — | — |  |
| `startTime` | `time` | NO | — | — | — |  |
| `endTime` | `time` | NO | — | — | — |  |
| `totalMarks` | `int` | NO | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — | created by |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `exams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `examTypeId` int NOT NULL,
  `instituteId` int NOT NULL,
  `instituteStreamClassId` int NOT NULL,
  `instituteStreamClassSubjectId` int NOT NULL,
  `examDate` date NOT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL,
  `totalMarks` int NOT NULL,
  `teacherId` int NOT NULL COMMENT 'created by',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=362 DEFAULT CHARSET=latin1
```

---

## 45. `exhibition_photos`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 5 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `exhibitionId` | `int` | NO | — | — | — |  |
| `picUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `exhibition_photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `exhibitionId` int NOT NULL,
  `picUrl` varchar(255) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1
```

---

## 46. `exhibitions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `studentId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `year` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `exhibitions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `studentId` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `desc` text,
  `year` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=latin1
```

---

## 47. `faculties`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 14 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `faculties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=36 DEFAULT CHARSET=latin1
```

---

## 48. `institute_entrance_exams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 33 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteFacultyId` | `int` | NO | — | — | — |  |
| `entranceName` | `varchar(255)` | NO | — | — | — |  |
| `examLink` | `varchar(255)` | NO | — | — | — |  |
| `merit` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_entrance_exams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `instituteFacultyId` int NOT NULL,
  `entranceName` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `examLink` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `merit` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 49. `institute_facilities`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 37 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | YES | — | — | — |  |
| `title` | `varchar(255)` | YES | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_facilities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int DEFAULT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `desc` text COLLATE utf8mb4_general_ci,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 50. `institute_faculties`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 122 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `facultyId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `timestamp` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_faculties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `facultyId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=147 DEFAULT CHARSET=latin1
```

---

## 51. `institute_fees`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 20 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteFacultyId` | `int` | NO | — | — | — |  |
| `instituteStreamId` | `int` | NO | — | — | — |  |
| `instituteClassId` | `int` | NO | — | — | — |  |
| `casteCategoryId` | `int` | NO | — | — | — |  |
| `fees` | `double` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_fees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `instituteFacultyId` int NOT NULL,
  `instituteStreamId` int NOT NULL,
  `instituteClassId` int NOT NULL,
  `casteCategoryId` int NOT NULL,
  `fees` double NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 52. `institute_galleries`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 216 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | YES | — | — | — |  |
| `photoPath` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_galleries` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int DEFAULT NULL,
  `photoPath` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=217 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 53. `institute_leads`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 8 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteStreamId` | `int` | NO | — | — | — |  |
| `mobile` | `varchar(255)` | NO | — | — | — |  |
| `email` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `status` | `smallint` | NO | 1 | — | — | 1 - pending/2 - interested/3 - Not responding/4 - Admission done/5 - Not interested |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_leads` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `instituteId` int NOT NULL,
  `instituteStreamId` int NOT NULL,
  `mobile` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `desc` text COLLATE utf8mb4_general_ci,
  `status` smallint NOT NULL DEFAULT '1' COMMENT '1 - pending/2 - interested/3 - Not responding/4 - Admission done/5 - Not interested',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 54. `institute_placed_students`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | YES | — | — | — |  |
| `institutePlacementCompanyId` | `varchar(255)` | YES | — | — | — |  |
| `studentId` | `int` | YES | — | — | — |  |
| `studentAvtar` | `varchar(255)` | YES | — | — | — |  |
| `package` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_placed_students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int DEFAULT NULL,
  `institutePlacementCompanyId` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `studentId` int DEFAULT NULL,
  `studentAvtar` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `package` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 55. `institute_placement_companies`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 85 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | YES | — | — | — |  |
| `companyName` | `varchar(255)` | YES | — | — | — |  |
| `companyLogo` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_placement_companies` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int DEFAULT NULL,
  `companyName` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `companyLogo` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=92 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 56. `institute_ratings`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 9 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `placement` | `double` | YES | — | — | — |  |
| `staff` | `double` | NO | — | — | — |  |
| `teaching` | `double` | NO | — | — | — |  |
| `environment` | `double` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_ratings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `userId` int NOT NULL,
  `placement` double DEFAULT NULL,
  `staff` double NOT NULL,
  `teaching` double NOT NULL,
  `environment` double NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 57. `institute_stream_class_subject_teachers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 45 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteStreamClassId` | `int` | NO | — | — | — |  |
| `subjectName` | `varchar(255)` | NO | — | — | — |  |
| `subjectShortName` | `varchar(255)` | NO | — | — | — |  |
| `teacherId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_stream_class_subject_teachers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteStreamClassId` int NOT NULL,
  `subjectName` varchar(255) NOT NULL,
  `subjectShortName` varchar(255) NOT NULL,
  `teacherId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=latin1
```

---

## 58. `institute_stream_classes`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2,496 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteFacultyId` | `int` | NO | — | — | — |  |
| `instituteStreamId` | `int` | NO | — | — | — |  |
| `parentInstituteStreamClassId` | `int` | YES | — | — | — |  |
| `className` | `varchar(255)` | NO | — | — | — |  |
| `division` | `varchar(255)` | YES | — | — | — |  |
| `classTeacherId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_stream_classes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `instituteFacultyId` int NOT NULL,
  `instituteStreamId` int NOT NULL,
  `parentInstituteStreamClassId` int DEFAULT NULL,
  `className` varchar(255) NOT NULL,
  `division` varchar(255) DEFAULT NULL,
  `classTeacherId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2555 DEFAULT CHARSET=latin1
```

---

## 59. `institute_streams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 491 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteFacultyId` | `int` | NO | — | — | — |  |
| `streamId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `timestamp` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_streams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `instituteFacultyId` int NOT NULL,
  `streamId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` timestamp NULL DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=496 DEFAULT CHARSET=latin1
```

---

## 60. `institute_trip_photos`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 36 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteTripId` | `int` | NO | — | — | — |  |
| `picUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_trip_photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteTripId` int NOT NULL,
  `picUrl` varchar(255) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=latin1
```

---

## 61. `institute_trips`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `tripDate` | `date` | NO | — | — | — |  |
| `managedBy` | `int` | NO | — | — | — | Teacher who managed |
| `totalStudent` | `int` | NO | — | — | — |  |
| `tripDetails` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_trips` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `tripDate` date NOT NULL,
  `managedBy` int NOT NULL COMMENT 'Teacher who managed',
  `totalStudent` int NOT NULL,
  `tripDetails` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=latin1
```

---

## 62. `institute_types`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institute_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

---

## 63. `institutes`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 78 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `instituteTypeId` | `int` | YES | — | — | — |  |
| `instituteName` | `varchar(255)` | YES | — | — | — |  |
| `instituteUsername` | `varchar(255)` | YES | — | — | — |  |
| `website` | `varchar(255)` | YES | — | — | — |  |
| `aboutUs` | `text` | YES | — | — | — |  |
| `policy` | `text` | YES | — | — | — |  |
| `deanId` | `int` | YES | — | — | — |  |
| `deanEducation` | `text` | YES | — | — | — |  |
| `assignDeanDate` | `datetime` | YES | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `brochurePath` | `varchar(255)` | YES | — | — | — |  |
| `bannerPath` | `varchar(255)` | YES | — | — | — |  |
| `stateId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `institutes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `instituteTypeId` int DEFAULT NULL,
  `instituteName` varchar(255) DEFAULT NULL,
  `instituteUsername` varchar(255) DEFAULT NULL,
  `website` varchar(255) DEFAULT NULL,
  `aboutUs` text,
  `policy` text,
  `deanId` int DEFAULT NULL,
  `deanEducation` text CHARACTER SET latin1 COLLATE latin1_swedish_ci,
  `assignDeanDate` datetime DEFAULT NULL,
  `desc` text,
  `brochurePath` varchar(255) DEFAULT NULL,
  `bannerPath` varchar(255) DEFAULT NULL,
  `stateId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=85 DEFAULT CHARSET=latin1
```

---

## 64. `lectures`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteStreamClassId` | `int` | YES | — | — | — |  |
| `instituteStreamClassSubjectId` | `int` | YES | — | — | — |  |
| `lectureDate` | `date` | NO | — | — | — |  |
| `lectureStartTime` | `time` | NO | — | — | — |  |
| `lectureEndTime` | `time` | NO | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `lectures` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteStreamClassId` int DEFAULT NULL,
  `instituteStreamClassSubjectId` int DEFAULT NULL,
  `lectureDate` date NOT NULL,
  `lectureStartTime` time NOT NULL,
  `lectureEndTime` time NOT NULL,
  `teacherId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1
```

---

## 65. `login_histories`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_0900_ai_ci |
| Approx. Rows | 1,978 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `token` | `text` | NO | — | — | — |  |
| `logoutReason` | `varchar(255)` | YES | — | — | — | 1 - Self Logout/2 - Login another device/3 - Account disable |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `login_histories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `token` text NOT NULL,
  `logoutReason` varchar(255) DEFAULT NULL COMMENT '1 - Self Logout/2 - Login another device/3 - Account disable',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2031 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci
```

---

## 66. `message_deletions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 3,058 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `messageId` | `int` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `message_deletions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `messageId` int NOT NULL,
  `userId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3059 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 67. `messages`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 3,857 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `roomId` | `text` | YES | — | — | — |  |
| `parentId` | `int` | YES | — | — | — |  |
| `senderUserId` | `int` | YES | — | — | — |  |
| `receiverUserId` | `int` | YES | — | — | — |  |
| `sharedPostId` | `int` | YES | — | — | — |  |
| `file` | `varchar(255)` | YES | — | — | — |  |
| `message` | `text` | YES | — | — | — |  |
| `deliveredAt` | `timestamp` | YES | — | — | — |  |
| `seenAt` | `datetime` | YES | — | — | — |  |
| `isTextUpdate` | `datetime` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `messages` (
  `id` int NOT NULL AUTO_INCREMENT,
  `roomId` text COLLATE utf8mb4_general_ci,
  `parentId` int DEFAULT NULL,
  `senderUserId` int DEFAULT NULL,
  `receiverUserId` int DEFAULT NULL,
  `sharedPostId` int DEFAULT NULL,
  `file` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `message` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci,
  `deliveredAt` timestamp NULL DEFAULT NULL,
  `seenAt` datetime DEFAULT NULL,
  `isTextUpdate` datetime DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3841 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 68. `mock_exam_faculties`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 8 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `mockExamId` | `int` | NO | — | — | — |  |
| `facultyId` | `int` | YES | — | — | — |  |
| `email` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exam_faculties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mockExamId` int NOT NULL,
  `facultyId` int DEFAULT NULL,
  `email` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 69. `mock_exam_questions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 846 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `mockExamSubjectId` | `int` | NO | — | — | — |  |
| `questionId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exam_questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mockExamSubjectId` int NOT NULL,
  `questionId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=967 DEFAULT CHARSET=latin1
```

---

## 70. `mock_exam_streams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `mockExamId` | `int` | NO | — | — | — |  |
| `streamId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exam_streams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mockExamId` int NOT NULL,
  `streamId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 71. `mock_exam_subject_faculties`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 6 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `mockExamSubjectId` | `int` | NO | — | — | — |  |
| `facultyId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exam_subject_faculties` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mockExamSubjectId` int NOT NULL,
  `facultyId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 72. `mock_exam_subject_streams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `mockExamSubjectId` | `int` | NO | — | — | — |  |
| `streamId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exam_subject_streams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mockExamSubjectId` int NOT NULL,
  `streamId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 73. `mock_exam_subjects`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 39 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `mockExamId` | `int` | NO | — | — | — |  |
| `subject` | `varchar(255)` | YES | — | — | — |  |
| `totalMarks` | `int` | YES | — | — | — |  |
| `scheduleStartTime` | `datetime` | YES | — | — | — |  |
| `scheduleEndTime` | `datetime` | YES | — | — | — |  |
| `solvingMinutes` | `int` | YES | — | — | — |  |
| `status` | `smallint` | YES | — | — | — | 1 - Active/2 - Inactive |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exam_subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `mockExamId` int NOT NULL,
  `subject` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `totalMarks` int DEFAULT NULL,
  `scheduleStartTime` datetime DEFAULT NULL,
  `scheduleEndTime` datetime DEFAULT NULL,
  `solvingMinutes` int DEFAULT NULL,
  `status` smallint DEFAULT NULL COMMENT '1 - Active/2 - Inactive',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 74. `mock_exams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 11 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `examName` | `varchar(255)` | NO | — | — | — |  |
| `avtarUrl` | `varchar(255)` | YES | — | — | — |  |
| `facultyId` | `int` | NO | — | — | — |  |
| `status` | `smallint` | NO | 1 | — | — | 1 - active/2 - Inactive |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `mock_exams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `examName` varchar(255) NOT NULL,
  `avtarUrl` varchar(255) DEFAULT NULL,
  `facultyId` int NOT NULL,
  `status` smallint NOT NULL DEFAULT '1' COMMENT '1 - active/2 - Inactive',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=latin1
```

---

## 75. `news_paper_categories`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `news_paper_categories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1
```

---

## 76. `news_papers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `newsPaperCategoryId` | `int` | NO | — | — | — |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `thumbnailUrl` | `varchar(255)` | YES | — | — | — |  |
| `paperUrl` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `news_papers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `newsPaperCategoryId` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `thumbnailUrl` varchar(255) DEFAULT NULL,
  `paperUrl` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1
```

---

## 77. `notifications`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 305 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `moduleType` | `smallint` | YES | — | — | — | 1 - admin/2 - institute/ 3 - user |
| `userId` | `int` | NO | — | — | — |  |
| `actionBy` | `int` | NO | — | — | — |  |
| `notification` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `notifications` (
  `id` int NOT NULL AUTO_INCREMENT,
  `moduleType` smallint DEFAULT NULL COMMENT '1 - admin/2 - institute/ 3 - user',
  `userId` int NOT NULL,
  `actionBy` int NOT NULL,
  `notification` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=318 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 78. `opportunities`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | YES | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `opportunities` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1
```

---

## 79. `opportunity_candidates`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 8 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `opportunityId` | `int` | NO | — | — | — |  |
| `studentId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `opportunity_candidates` (
  `id` int NOT NULL AUTO_INCREMENT,
  `opportunityId` int NOT NULL,
  `studentId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1
```

---

## 80. `post_comments`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 127 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `postId` | `int` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `comment` | `text` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `post_comments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `postId` int NOT NULL,
  `userId` int NOT NULL,
  `comment` text COLLATE utf8mb4_general_ci NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=291 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 81. `post_likes`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 1,785 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `postId` | `int` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `post_likes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `postId` int NOT NULL,
  `userId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2298 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 82. `post_photos`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 535 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `postId` | `varchar(255)` | YES | — | — | — |  |
| `pathUrl` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `post_photos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `postId` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `pathUrl` varchar(255) COLLATE utf8mb4_general_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=541 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 83. `posts`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 432 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `shortId` | `varchar(255)` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `posts` (
  `id` int NOT NULL AUTO_INCREMENT,
  `shortId` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `userId` int NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `desc` text COLLATE utf8mb4_general_ci,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=433 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 84. `question_options`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 18,776 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `questionId` | `int` | NO | — | — | — |  |
| `answer` | `text` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `question_options` (
  `id` int NOT NULL AUTO_INCREMENT,
  `questionId` int NOT NULL,
  `answer` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19100 DEFAULT CHARSET=latin1
```

---

## 85. `questions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4,685 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `questionType` | `int` | NO | — | — | — | 1 - Objective/2 - Subjective |
| `question` | `text` | NO | — | — | — |  |
| `answerId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `questionType` int NOT NULL COMMENT '1 - Objective/2 - Subjective',
  `question` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `answerId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5443 DEFAULT CHARSET=latin1
```

---

## 86. `report_cards`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 38 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `studentId` | `int` | NO | — | — | — |  |
| `instituteStreamClassId` | `int` | YES | — | — | — |  |
| `reportCardUrl` | `varchar(255)` | YES | — | — | — |  |
| `teacherId` | `int` | YES | — | — | — | Added by teacher |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `report_cards` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentId` int NOT NULL,
  `instituteStreamClassId` int DEFAULT NULL,
  `reportCardUrl` varchar(255) DEFAULT NULL,
  `teacherId` int DEFAULT NULL COMMENT 'Added by teacher',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=latin1
```

---

## 87. `reports`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 39 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `itemId` | `int` | NO | — | — | — |  |
| `reportOn` | `int` | NO | — | — | — | 1 - Post/2 - User |
| `userId` | `int` | NO | — | — | — |  |
| `report` | `varchar(255)` | NO | — | — | — |  |
| `status` | `smallint` | NO | 1 | — | — | 1 - Pending/2 - Resolve |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `reports` (
  `id` int NOT NULL AUTO_INCREMENT,
  `itemId` int NOT NULL,
  `reportOn` int NOT NULL COMMENT '1 - Post/2 - User',
  `userId` int NOT NULL,
  `report` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `status` smallint NOT NULL DEFAULT '1' COMMENT '1 - Pending/2 - Resolve',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 88. `sequelizemeta`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb3_unicode_ci |
| Approx. Rows | 79 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `name` | `varchar(255)` | NO | — | PRI | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `name` | ✅ | BTREE | `name` |
| `PRIMARY` | ✅ | BTREE | `name` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `sequelizemeta` (
  `name` varchar(255) COLLATE utf8mb3_unicode_ci NOT NULL,
  PRIMARY KEY (`name`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3 COLLATE=utf8mb3_unicode_ci
```

---

## 89. `sport_accessories`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 1 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `accessories` | `text` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `sport_accessories` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `accessories` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin NOT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

---

## 90. `sport_competitions`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `provided` | `text` | YES | — | — | — |  |
| `banners` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `sport_competitions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `provided` text CHARACTER SET utf8mb4 COLLATE utf8mb4_bin,
  `banners` varchar(255) NOT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

---

## 91. `sport_teams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 6 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — |  |
| `position` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `sport_teams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `teacherId` int NOT NULL,
  `position` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1
```

---

## 92. `states`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 36 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `states` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=37 DEFAULT CHARSET=latin1
```

---

## 93. `streams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 232 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `facultyId` | `int` | NO | — | — | — |  |
| `streamName` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `streams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `facultyId` int NOT NULL,
  `streamName` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=592 DEFAULT CHARSET=latin1
```

---

## 94. `student_assignment_question_answers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 1,165 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `studentAssignmentId` | `varchar(255)` | NO | — | — | — |  |
| `assignmentQuestionId` | `varchar(255)` | YES | — | — | — |  |
| `selectedAnswerId` | `varchar(255)` | YES | — | — | — |  |
| `answer` | `text` | YES | — | — | — |  |
| `isCorrect` | `smallint` | YES | 2 | — | — | 1 - Correct/ 2 - Wrong |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `student_assignment_question_answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentAssignmentId` varchar(255) NOT NULL,
  `assignmentQuestionId` varchar(255) DEFAULT NULL,
  `selectedAnswerId` varchar(255) DEFAULT NULL,
  `answer` text,
  `isCorrect` smallint DEFAULT '2' COMMENT '1 - Correct/ 2 - Wrong',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2160 DEFAULT CHARSET=latin1
```

---

## 95. `student_assignments`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 216 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `studentId` | `int` | NO | — | — | — |  |
| `assignmentId` | `int` | NO | — | — | — |  |
| `totalMarks` | `double` | NO | — | — | — |  |
| `obtainMarks` | `double` | NO | — | — | — |  |
| `status` | `smallint` | NO | — | — | — | 1 - Pending check/2 - Completed check |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `student_assignments` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentId` int NOT NULL,
  `assignmentId` int NOT NULL,
  `totalMarks` double NOT NULL,
  `obtainMarks` double NOT NULL,
  `status` smallint NOT NULL COMMENT '1 - Pending check/2 - Completed check',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=219 DEFAULT CHARSET=latin1
```

---

## 96. `student_attendances`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2,223 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `studentId` | `int` | NO | — | — | — |  |
| `attendanceDate` | `date` | NO | — | — | — |  |
| `present` | `smallint` | NO | 2 | — | — | 1 - Present/2 - Absent |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteStreamClassId` | `int` | NO | — | — | — |  |
| `instituteStreamClassSubjectId` | `int` | NO | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — | attendance added by teacher |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `student_attendances` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentId` int NOT NULL,
  `attendanceDate` date NOT NULL,
  `present` smallint NOT NULL DEFAULT '2' COMMENT '1 - Present/2 - Absent',
  `instituteId` int NOT NULL,
  `instituteStreamClassId` int NOT NULL,
  `instituteStreamClassSubjectId` int NOT NULL,
  `teacherId` int NOT NULL COMMENT 'attendance added by teacher',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2251 DEFAULT CHARSET=latin1
```

---

## 97. `student_exam_question_answers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 3,338 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `studentExamId` | `varchar(255)` | NO | — | — | — |  |
| `examQuestionId` | `int` | YES | — | — | — |  |
| `selectedAnswerId` | `int` | YES | — | — | — |  |
| `isCorrect` | `smallint` | YES | 2 | — | — | 1 - Correct/ 2 - Wrong |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `student_exam_question_answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentExamId` varchar(255) NOT NULL,
  `examQuestionId` int DEFAULT NULL,
  `selectedAnswerId` int DEFAULT NULL,
  `isCorrect` smallint DEFAULT '2' COMMENT '1 - Correct/ 2 - Wrong',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3468 DEFAULT CHARSET=latin1
```

---

## 98. `student_exams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 211 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `studentId` | `int` | NO | — | — | — |  |
| `examId` | `int` | NO | — | — | — |  |
| `totalMarks` | `int` | NO | — | — | — |  |
| `obtainMarks` | `double` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `student_exams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `studentId` int NOT NULL,
  `examId` int NOT NULL,
  `totalMarks` int NOT NULL,
  `obtainMarks` double DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=237 DEFAULT CHARSET=latin1
```

---

## 99. `students`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 892 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteFacultyId` | `int` | NO | — | — | — |  |
| `instituteStreamId` | `int` | NO | — | — | — |  |
| `instituteStreamClassId` | `int` | NO | — | — | — |  |
| `rollNumber` | `varchar(255)` | YES | — | — | — |  |
| `userName` | `varchar(100)` | YES | — | — | — |  |
| `firstName` | `varchar(255)` | NO | — | — | — |  |
| `lastName` | `varchar(255)` | NO | — | — | — |  |
| `email` | `varchar(255)` | YES | — | — | — |  |
| `mobile` | `varchar(255)` | NO | — | — | — |  |
| `approvedByInstite` | `datetime` | YES | — | — | — |  |
| `rejectByInstitute` | `datetime` | YES | — | — | — |  |
| `status` | `int` | YES | 1 | — | — | 1 - Active/ 2 - Inactive |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `students` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `instituteId` int NOT NULL,
  `instituteFacultyId` int NOT NULL,
  `instituteStreamId` int NOT NULL,
  `instituteStreamClassId` int NOT NULL,
  `rollNumber` varchar(255) DEFAULT NULL,
  `userName` varchar(100) DEFAULT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) NOT NULL,
  `approvedByInstite` datetime DEFAULT NULL,
  `rejectByInstitute` datetime DEFAULT NULL,
  `status` int DEFAULT '1' COMMENT '1 - Active/ 2 - Inactive',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=893 DEFAULT CHARSET=latin1
```

---

## 100. `subjects`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 0 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `subjects` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) COLLATE utf8mb4_general_ci NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 101. `teachers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 76 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteFacultyId` | `int` | YES | — | — | — |  |
| `instituteStreamId` | `int` | YES | — | — | — |  |
| `firstName` | `varchar(255)` | NO | — | — | — |  |
| `lastName` | `varchar(255)` | NO | — | — | — |  |
| `email` | `varchar(255)` | YES | — | — | — |  |
| `mobile` | `varchar(255)` | YES | — | — | — |  |
| `picUrl` | `varchar(255)` | YES | — | — | — |  |
| `approvedByInstite` | `datetime` | YES | — | — | — |  |
| `rejectByInstitute` | `datetime` | YES | — | — | — |  |
| `status` | `int` | YES | — | — | — | 1 - Active/ 2 - Inactive |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `teachers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `instituteId` int NOT NULL,
  `instituteFacultyId` int DEFAULT NULL,
  `instituteStreamId` int DEFAULT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `email` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `picUrl` varchar(255) DEFAULT NULL,
  `approvedByInstite` datetime DEFAULT NULL,
  `rejectByInstitute` datetime DEFAULT NULL,
  `status` int DEFAULT NULL COMMENT '1 - Active/ 2 - Inactive',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=79 DEFAULT CHARSET=latin1
```

---

## 102. `timetables`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 122 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `instituteStreamClassId` | `int` | NO | — | — | — |  |
| `instituteStreamClassSubjectId` | `int` | NO | — | — | — |  |
| `scheduleDate` | `date` | YES | — | — | — |  |
| `startTime` | `time` | NO | — | — | — |  |
| `endTime` | `time` | NO | — | — | — |  |
| `scheduleDays` | `varchar(255)` | YES | — | — | — |  |
| `teacherId` | `int` | NO | — | — | — | created by  |
| `desc` | `text` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `timetables` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `instituteStreamClassId` int NOT NULL,
  `instituteStreamClassSubjectId` int NOT NULL,
  `scheduleDate` date DEFAULT NULL,
  `startTime` time NOT NULL,
  `endTime` time NOT NULL,
  `scheduleDays` varchar(255) DEFAULT NULL,
  `teacherId` int NOT NULL COMMENT 'created by ',
  `desc` text NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=123 DEFAULT CHARSET=latin1
```

---

## 103. `transport_details`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 2 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `title` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `transport_details` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `title` varchar(255) NOT NULL,
  `desc` text,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

---

## 104. `transport_fees`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 4 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `fromLocation` | `varchar(255)` | NO | — | — | — |  |
| `toLocation` | `varchar(255)` | NO | — | — | — |  |
| `desc` | `text` | YES | — | — | — |  |
| `fees` | `double` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `transport_fees` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `fromLocation` varchar(255) NOT NULL,
  `toLocation` varchar(255) NOT NULL,
  `desc` text,
  `fees` double NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1
```

---

## 105. `transport_teams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 9 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `instituteId` | `int` | NO | — | — | — |  |
| `userId` | `int` | NO | — | — | — |  |
| `position` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `transport_teams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instituteId` int NOT NULL,
  `userId` int NOT NULL,
  `position` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=latin1
```

---

## 106. `user_block_users`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 72 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | YES | — | — | — |  |
| `blockUserId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_block_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int DEFAULT NULL,
  `blockUserId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=76 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 107. `user_connections`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 1,492 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `senderUserId` | `int` | NO | — | — | — |  |
| `receiverUserId` | `int` | NO | — | — | — |  |
| `status` | `smallint` | YES | 1 | — | — | 1 - Pending/ 2 - Accepted/ 3 - Rejacted |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_connections` (
  `id` int NOT NULL AUTO_INCREMENT,
  `senderUserId` int NOT NULL,
  `receiverUserId` int NOT NULL,
  `status` smallint DEFAULT '1' COMMENT '1 - Pending/ 2 - Accepted/ 3 - Rejacted',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1493 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 108. `user_favourite_institutes`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 176 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `varchar(255)` | YES | — | — | — |  |
| `instituteId` | `varchar(255)` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_favourite_institutes` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` varchar(255) DEFAULT NULL,
  `instituteId` varchar(255) DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=181 DEFAULT CHARSET=latin1
```

---

## 109. `user_mock_exam_question_answers`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 5,574 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userMockExamId` | `varchar(255)` | NO | — | — | — |  |
| `mockExamQuestionId` | `varchar(255)` | YES | — | — | — |  |
| `selectedAnswerId` | `varchar(255)` | YES | — | — | — |  |
| `isCorrect` | `smallint` | YES | 2 | — | — | 1 - Correct/ 2 - Wrong |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_mock_exam_question_answers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userMockExamId` varchar(255) NOT NULL,
  `mockExamQuestionId` varchar(255) DEFAULT NULL,
  `selectedAnswerId` varchar(255) DEFAULT NULL,
  `isCorrect` smallint DEFAULT '2' COMMENT '1 - Correct/ 2 - Wrong',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5575 DEFAULT CHARSET=latin1
```

---

## 110. `user_mock_exams`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 142 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `mockExamSubjectId` | `int` | NO | — | — | — |  |
| `totalMarks` | `int` | NO | — | — | — |  |
| `obtainMarks` | `double` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_mock_exams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `mockExamSubjectId` int NOT NULL,
  `totalMarks` int NOT NULL,
  `obtainMarks` double DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=153 DEFAULT CHARSET=latin1
```

---

## 111. `user_notification_settings`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 43 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `personalMessage` | `smallint` | YES | 1 | — | — |  |
| `groupMessage` | `smallint` | YES | 1 | — | — |  |
| `post` | `smallint` | YES | 1 | — | — |  |
| `assignment` | `smallint` | YES | 1 | — | — |  |
| `teachingPlan` | `smallint` | YES | 1 | — | — |  |
| `complaintBox` | `smallint` | YES | 1 | — | — |  |
| `systemNotification` | `smallint` | YES | 1 | — | — |  |
| `autoAcceptRequest` | `smallint` | YES | — | — | — |  |
| `exam` | `smallint` | YES | 1 | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_notification_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `personalMessage` smallint DEFAULT '1',
  `groupMessage` smallint DEFAULT '1',
  `post` smallint DEFAULT '1',
  `assignment` smallint DEFAULT '1',
  `teachingPlan` smallint DEFAULT '1',
  `complaintBox` smallint DEFAULT '1',
  `systemNotification` smallint DEFAULT '1',
  `autoAcceptRequest` smallint DEFAULT NULL,
  `exam` smallint DEFAULT '1',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 112. `user_privacy_settings`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | utf8mb4_general_ci |
| Approx. Rows | 1,719 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `profilePicture` | `smallint` | YES | 1 | — | — |  |
| `mobileNumber` | `smallint` | YES | 1 | — | — |  |
| `email` | `smallint` | YES | 1 | — | — |  |
| `dob` | `smallint` | YES | 1 | — | — |  |
| `aboutBio` | `smallint` | YES | 1 | — | — |  |
| `isPublicAccount` | `smallint` | NO | 1 | — | — | 0-Not Public/ 1 - Public |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_privacy_settings` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `profilePicture` smallint DEFAULT '1',
  `mobileNumber` smallint DEFAULT '1',
  `email` smallint DEFAULT '1',
  `dob` smallint DEFAULT '1',
  `aboutBio` smallint DEFAULT '1',
  `isPublicAccount` smallint NOT NULL DEFAULT '1' COMMENT '0-Not Public/ 1 - Public',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1720 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci
```

---

## 113. `user_recent_books`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 501 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | NO | — | — | — |  |
| `bookId` | `int` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_recent_books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int NOT NULL,
  `bookId` int NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=502 DEFAULT CHARSET=latin1
```

---

## 114. `user_save_books`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 90 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userId` | `int` | YES | — | — | — |  |
| `bookId` | `int` | YES | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_save_books` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userId` int DEFAULT NULL,
  `bookId` int DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=287 DEFAULT CHARSET=latin1
```

---

## 115. `user_types`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 3 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `name` | `varchar(255)` | NO | — | — | — |  |
| `keyName` | `varchar(255)` | NO | — | — | — |  |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `user_types` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `keyName` varchar(255) NOT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1
```

---

## 116. `users`

| Property | Value |
|----------|-------|
| Engine | InnoDB |
| Collation | latin1_swedish_ci |
| Approx. Rows | 1,716 |

### Columns

| Column | Type | Nullable | Default | Key | Extra | Comment |
|--------|------|----------|---------|-----|-------|---------|
| `id` | `int` | NO | — | PRI | auto_increment |  |
| `userTypeId` | `int` | NO | — | — | — |  |
| `userName` | `varchar(255)` | YES | — | — | — |  |
| `firstName` | `varchar(255)` | NO | — | — | — |  |
| `lastName` | `varchar(255)` | YES | — | — | — |  |
| `email` | `varchar(255)` | YES | — | — | — |  |
| `emailVerification` | `timestamp` | YES | — | — | — |  |
| `password` | `varchar(255)` | YES | — | — | — |  |
| `mobile` | `varchar(255)` | YES | — | — | — |  |
| `dob` | `date` | YES | — | — | — |  |
| `gender` | `enum('male','female','other')` | YES | — | — | — |  |
| `avtarUrl` | `varchar(255)` | YES | — | — | — |  |
| `address` | `varchar(255)` | YES | — | — | — |  |
| `stateId` | `int` | YES | — | — | — |  |
| `bloodGroup` | `varchar(100)` | YES | — | — | — |  |
| `bio` | `text` | YES | — | — | — |  |
| `hobbies` | `longtext` | YES | — | — | — |  |
| `skills` | `longtext` | YES | — | — | — |  |
| `achievements` | `longtext` | YES | — | — | — |  |
| `userDeleteAccount` | `datetime` | YES | — | — | — |  |
| `resetPasswordToken` | `varchar(255)` | YES | — | — | — |  |
| `pushNotificationToken` | `text` | YES | — | — | — |  |
| `status` | `smallint` | YES | 1 | — | — | 1 - active/2 - Inactive	 |
| `createdAt` | `datetime` | NO | — | — | — |  |
| `updatedAt` | `datetime` | NO | — | — | — |  |
| `deletedAt` | `datetime` | YES | — | — | — |  |

### Indexes

| Index Name | Unique | Type | Columns |
|------------|--------|------|---------|
| `PRIMARY` | ✅ | BTREE | `id` |

### Foreign Keys

_No foreign keys._

### DDL

```sql
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `userTypeId` int NOT NULL,
  `userName` varchar(255) DEFAULT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  `emailVerification` timestamp NULL DEFAULT NULL,
  `password` varchar(255) DEFAULT NULL,
  `mobile` varchar(255) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `gender` enum('male','female','other') DEFAULT NULL,
  `avtarUrl` varchar(255) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `stateId` int DEFAULT NULL,
  `bloodGroup` varchar(100) DEFAULT NULL,
  `bio` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `hobbies` longtext,
  `skills` longtext,
  `achievements` longtext,
  `userDeleteAccount` datetime DEFAULT NULL,
  `resetPasswordToken` varchar(255) DEFAULT NULL,
  `pushNotificationToken` text,
  `status` smallint DEFAULT '1' COMMENT '1 - active/2 - Inactive	',
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL,
  `deletedAt` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=1735 DEFAULT CHARSET=latin1
```
