#!/usr/bin/env python
"""
export_schema.py
================
Connects to the MySQL database and writes a full schema document to
  schema_<DATABASE>_<YYYYMMDD_HHMM>.md

Usage:
    python export_schema.py                  # reads credentials from .env
    python export_schema.py --output my.md  # custom output file
    python export_schema.py --table users   # single table only
    python export_schema.py --filter ai_    # tables whose name starts with ai_

Requires: pip install pymysql python-dotenv
"""

import argparse
import os
import sys
from datetime import datetime
from pathlib import Path

# ── Load .env ────────────────────────────────────────────────────────────────
try:
    from dotenv import load_dotenv
    load_dotenv(Path(__file__).resolve().parent / '.env')
except ImportError:
    pass  # python-dotenv not installed — rely on env vars being pre-set

try:
    import pymysql
    import pymysql.cursors
except ImportError:
    sys.exit("PyMySQL is not installed. Run: pip install PyMySQL")

# ── DB credentials from environment (fallback to .env values) ────────────────
DB_CONFIG = {
    'host':     os.environ.get('DATABASE_HOST', '194.164.148.150'),
    'port':     int(os.environ.get('DATABASE_PORT', 3306)),
    'user':     os.environ.get('DATABASE_USER', 'alpha-api'),
    'password': os.environ.get('DATABASE_PASSWORD', ''),
    'database': os.environ.get('DATABASE_NAME', 'alpha-api'),
    'charset':  'utf8mb4',
    'cursorclass': pymysql.cursors.DictCursor,
}

# ─────────────────────────────────────────────────────────────────────────────

def get_tables(cursor, name_filter: str | None, single_table: str | None) -> list[str]:
    if single_table:
        cursor.execute(
            "SELECT TABLE_NAME FROM information_schema.TABLES "
            "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s ORDER BY TABLE_NAME",
            (DB_CONFIG['database'], single_table)
        )
    elif name_filter:
        cursor.execute(
            "SELECT TABLE_NAME FROM information_schema.TABLES "
            "WHERE TABLE_SCHEMA = %s AND TABLE_NAME LIKE %s ORDER BY TABLE_NAME",
            (DB_CONFIG['database'], f"{name_filter}%")
        )
    else:
        cursor.execute(
            "SELECT TABLE_NAME FROM information_schema.TABLES "
            "WHERE TABLE_SCHEMA = %s ORDER BY TABLE_NAME",
            (DB_CONFIG['database'],)
        )
    return [row['TABLE_NAME'] for row in cursor.fetchall()]


def get_columns(cursor, table: str) -> list[dict]:
    cursor.execute(
        "SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_DEFAULT, "
        "EXTRA, COLUMN_KEY, COLUMN_COMMENT "
        "FROM information_schema.COLUMNS "
        "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s "
        "ORDER BY ORDINAL_POSITION",
        (DB_CONFIG['database'], table)
    )
    return cursor.fetchall()


def get_indexes(cursor, table: str) -> list[dict]:
    cursor.execute(
        "SELECT INDEX_NAME, NON_UNIQUE, SEQ_IN_INDEX, COLUMN_NAME, INDEX_TYPE "
        "FROM information_schema.STATISTICS "
        "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s "
        "ORDER BY INDEX_NAME, SEQ_IN_INDEX",
        (DB_CONFIG['database'], table)
    )
    return cursor.fetchall()


def get_foreign_keys(cursor, table: str) -> list[dict]:
    cursor.execute(
        "SELECT kcu.CONSTRAINT_NAME, kcu.COLUMN_NAME, "
        "kcu.REFERENCED_TABLE_NAME, kcu.REFERENCED_COLUMN_NAME, "
        "rc.UPDATE_RULE, rc.DELETE_RULE "
        "FROM information_schema.KEY_COLUMN_USAGE kcu "
        "JOIN information_schema.REFERENTIAL_CONSTRAINTS rc "
        "  ON rc.CONSTRAINT_NAME = kcu.CONSTRAINT_NAME "
        "  AND rc.CONSTRAINT_SCHEMA = kcu.TABLE_SCHEMA "
        "WHERE kcu.TABLE_SCHEMA = %s AND kcu.TABLE_NAME = %s "
        "  AND kcu.REFERENCED_TABLE_NAME IS NOT NULL "
        "ORDER BY kcu.CONSTRAINT_NAME, kcu.ORDINAL_POSITION",
        (DB_CONFIG['database'], table)
    )
    return cursor.fetchall()


def get_table_comment(cursor, table: str) -> str:
    cursor.execute(
        "SELECT TABLE_COMMENT, ENGINE, TABLE_ROWS, TABLE_COLLATION "
        "FROM information_schema.TABLES "
        "WHERE TABLE_SCHEMA = %s AND TABLE_NAME = %s",
        (DB_CONFIG['database'], table)
    )
    row = cursor.fetchone()
    return row or {}


def get_create_ddl(cursor, table: str) -> str:
    cursor.execute(f"SHOW CREATE TABLE `{table}`")
    row = cursor.fetchone()
    return row.get('Create Table', '')


# ── Markdown builders ─────────────────────────────────────────────────────────

def build_column_table(columns: list[dict]) -> str:
    lines = [
        "| Column | Type | Nullable | Default | Key | Extra | Comment |",
        "|--------|------|----------|---------|-----|-------|---------|",
    ]
    for col in columns:
        lines.append(
            f"| `{col['COLUMN_NAME']}` "
            f"| `{col['COLUMN_TYPE']}` "
            f"| {col['IS_NULLABLE']} "
            f"| {col['COLUMN_DEFAULT'] if col['COLUMN_DEFAULT'] is not None else '—'} "
            f"| {col['COLUMN_KEY'] or '—'} "
            f"| {col['EXTRA'] or '—'} "
            f"| {col['COLUMN_COMMENT'] or ''} |"
        )
    return "\n".join(lines)


def build_index_table(indexes: list[dict]) -> str:
    if not indexes:
        return "_No indexes found._"
    # Group columns per index
    grouped: dict[str, dict] = {}
    for idx in indexes:
        name = idx['INDEX_NAME']
        if name not in grouped:
            grouped[name] = {
                'unique': not idx['NON_UNIQUE'],
                'type':   idx['INDEX_TYPE'],
                'cols':   [],
            }
        grouped[name]['cols'].append(idx['COLUMN_NAME'])

    lines = [
        "| Index Name | Unique | Type | Columns |",
        "|------------|--------|------|---------|",
    ]
    for name, info in grouped.items():
        cols = ", ".join(f"`{c}`" for c in info['cols'])
        unique = "✅" if info['unique'] else "—"
        lines.append(f"| `{name}` | {unique} | {info['type']} | {cols} |")
    return "\n".join(lines)


def build_fk_table(fks: list[dict]) -> str:
    if not fks:
        return "_No foreign keys._"
    lines = [
        "| Constraint | Column | References | On Update | On Delete |",
        "|------------|--------|-----------|-----------|-----------|",
    ]
    for fk in fks:
        lines.append(
            f"| `{fk['CONSTRAINT_NAME']}` "
            f"| `{fk['COLUMN_NAME']}` "
            f"| `{fk['REFERENCED_TABLE_NAME']}`.`{fk['REFERENCED_COLUMN_NAME']}` "
            f"| {fk['UPDATE_RULE']} "
            f"| {fk['DELETE_RULE']} |"
        )
    return "\n".join(lines)


def build_table_section(cursor, table: str, index: int) -> str:
    meta    = get_table_comment(cursor, table)
    columns = get_columns(cursor, table)
    indexes = get_indexes(cursor, table)
    fks     = get_foreign_keys(cursor, table)
    ddl     = get_create_ddl(cursor, table)

    comment = meta.get('TABLE_COMMENT', '') or ''
    engine  = meta.get('ENGINE', '')
    rows    = meta.get('TABLE_ROWS', 0)
    collation = meta.get('TABLE_COLLATION', '')

    lines = [
        f"---",
        f"",
        f"## {index}. `{table}`",
        f"",
    ]

    if comment:
        lines.append(f"> {comment}")
        lines.append("")

    lines += [
        f"| Property | Value |",
        f"|----------|-------|",
        f"| Engine | {engine} |",
        f"| Collation | {collation} |",
        f"| Approx. Rows | {rows:,} |",
        f"",
        f"### Columns",
        f"",
        build_column_table(columns),
        f"",
        f"### Indexes",
        f"",
        build_index_table(indexes),
        f"",
        f"### Foreign Keys",
        f"",
        build_fk_table(fks),
        f"",
        f"### DDL",
        f"",
        f"```sql",
        ddl,
        f"```",
        f"",
    ]
    return "\n".join(lines)


# ── Table of Contents ─────────────────────────────────────────────────────────

def build_toc(tables: list[str]) -> str:
    lines = ["## Table of Contents", ""]
    for i, t in enumerate(tables, 1):
        anchor = t.lower().replace('_', '-')
        lines.append(f"{i}. [`{t}`](#{i}-{anchor})")
    lines.append("")
    return "\n".join(lines)


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Export MySQL database schema to Markdown")
    parser.add_argument('--output', '-o', help="Output file path (default: auto-generated)")
    parser.add_argument('--table',  '-t', help="Export a single table by name")
    parser.add_argument('--filter', '-f', help="Export only tables whose name starts with this prefix")
    args = parser.parse_args()

    print(f"Connecting to {DB_CONFIG['host']}:{DB_CONFIG['port']} / {DB_CONFIG['database']} …")

    conn = pymysql.connect(**DB_CONFIG)

    try:
        with conn.cursor() as cursor:
            tables = get_tables(cursor, args.filter, args.table)

        if not tables:
            sys.exit("No tables found matching the given criteria.")

        print(f"Found {len(tables)} table(s). Generating schema …")

        now = datetime.now()
        timestamp = now.strftime('%Y-%m-%d %H:%M')
        file_ts   = now.strftime('%Y%m%d_%H%M')

        output_path = args.output or f"schema_{DB_CONFIG['database']}_{file_ts}.md"

        doc_lines = [
            f"# Database Schema — `{DB_CONFIG['database']}`",
            f"",
            f"**Generated:** {timestamp}  ",
            f"**Host:** `{DB_CONFIG['host']}:{DB_CONFIG['port']}`  ",
            f"**Tables exported:** {len(tables)}  ",
            f"",
            build_toc(tables),
        ]

        with conn.cursor() as cursor:
            for i, table in enumerate(tables, 1):
                print(f"  [{i:>3}/{len(tables)}] {table}")
                doc_lines.append(build_table_section(cursor, table, i))

        Path(output_path).write_text("\n".join(doc_lines), encoding='utf-8')
        print(f"\nSchema written to: {output_path}")

    finally:
        conn.close()


if __name__ == '__main__':
    main()
