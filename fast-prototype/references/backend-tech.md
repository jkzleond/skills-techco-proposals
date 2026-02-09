# Backend Technical Documentation Template

Template for backend development technical documentation.

---

## Document Structure

```markdown
# [Project Name] Backend Technical Documentation

## 1. Tech Stack
## 2. System Architecture
## 3. Database Design
## 4. API Documentation
## 5. Business Logic
## 6. Security Design
## 7. Performance Optimization
## 8. Deployment & Operations
```

---

## 1. Tech Stack

```yaml
Language: Node.js / Python / Java / Go
Framework: NestJS / FastAPI / Spring Boot / Gin
Database: PostgreSQL 14+
Cache: Redis 6+
Queue: RabbitMQ / Kafka
Storage: OSS / S3
Monitoring: Prometheus + Grafana
```

---

## 2. System Architecture

### 2.1 Overall Architecture

```
Client (Web/Mobile)
       ↓ HTTPS
    Load Balancer (Nginx)
       ↓
    Application Servers (API Server)
       ↓
┌──────┼──────┬──────┬──────┐
│      │      │      │      │
DB    Cache  Queue  Storage
(PG)  (Redis) (RMQ)  (OSS)
```

### 2.2 Layered Architecture

```
┌─────────────────────────────┐
│      Controller Layer       │  (Routing, Validation)
├─────────────────────────────┤
│       Service Layer         │  (Business Logic)
├─────────────────────────────┤
│     Repository Layer        │  (Data Access)
├─────────────────────────────┤
│      Database Layer         │  (Data Storage)
└─────────────────────────────┘
```

### 2.3 Module Organization

```yaml
User Module:
  - User registration
  - User login
  - User management
  - Permission control

Customer Module:
  - Customer CRUD
  - Customer categories
  - Import/Export

Sales Module:
  - Follow-up records
  - Sales opportunities
  - Task reminders

Data Module:
  - Statistics
  - Reports
  - Analytics
```

---

## 3. Database Design

### 3.1 Database Schema

**Users Table**
```sql
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL,
    email VARCHAR(100) UNIQUE,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    status VARCHAR(20) NOT NULL DEFAULT 'active',
    created_at TIMESTAMP NOT NULL DEFAULT NOW()
);

CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);
```

**Customers Table**
```sql
CREATE TABLE customers (
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    company VARCHAR(200),
    phone VARCHAR(20),
    email VARCHAR(100),
    tags TEXT[],
    user_id BIGINT NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT NOW(),
    FOREIGN KEY (user_id) REFERENCES users(id)
);

CREATE INDEX idx_customers_user_id ON customers(user_id);
CREATE INDEX idx_customers_tags ON customers USING GIN(tags);
```

### 3.2 Index Strategy

```yaml
Index principles:
  1. Index WHERE clause columns
  2. Index JOIN clause columns
  3. Index ORDER BY columns
  4. Use composite indexes for multi-condition queries

Index types:
  - B-tree: Default
  - Hash: Equality queries
  - GIN: Arrays, JSON
```

---

## 4. API Documentation

### 4.1 RESTful Standards

```yaml
URL design:
  - Use plural nouns: /users, /customers
  - Use lowercase: /user-profile
  - Use hyphens: /follow-records
  - Max 3 levels deep: /users/1/customers

HTTP methods:
  - GET: Query resources
  - POST: Create resources
  - PUT: Update (full)
  - PATCH: Update (partial)
  - DELETE: Delete resources
```

### 4.2 Request Format

**Headers**:
```yaml
Content-Type: application/json
Authorization: Bearer {token}
Accept: application/json
```

**Query params**:
```yaml
Pagination: page=1&pageSize=20
Sorting: sort=createdAt&order=desc
Filtering: status=active&role=admin
```

### 4.3 Response Format

**Success response**:
```json
{
  "code": 200,
  "message": "成功",
  "data": {},
  "timestamp": "2024-01-01T00:00:00Z"
}
```

**Error response**:
```json
{
  "code": 400,
  "message": "请求参数错误",
  "errors": [{
    "field": "username",
    "message": "用户名不能为空"
  }]
}
```

### 4.4 API Examples

**User Login**
```
POST /api/auth/login

Request:
{
  "username": "admin",
  "password": "123456"
}

Response:
{
  "code": 200,
  "data": {
    "token": "eyJhbG...",
    "user": {
      "id": 1,
      "username": "admin"
    }
  }
}
```

**Get Customers**
```
GET /api/customers?page=1&pageSize=20

Response:
{
  "code": 200,
  "data": {
    "list": [...],
    "total": 100,
    "page": 1,
    "pageSize": 20
  }
}
```

---

## 5. Business Logic

### 5.1 Authentication

```yaml
Flow:
  1. User submits credentials
  2. Server validates username/password
  3. Generate JWT token
  4. Return token and user info

JWT config:
  - Algorithm: HS256
  - Expiry: 7 days
  - Payload: userId, username, role

Password encryption:
  - Algorithm: bcrypt
  - Salt rounds: 10
```

### 5.2 Authorization

```yaml
Model: RBAC (Role-Based Access Control)

Roles:
  - admin: All permissions
  - user: Partial permissions
  - readonly: View only

Permission check:
  - Route level: Middleware
  - Controller level: Decorator
  - Data level: Business logic
```

### 5.3 Data Validation

```yaml
Rules:
  - Username: 3-50 chars, alphanumeric
  - Email: Standard email format
  - Phone: 11 digits
  - Password: 6-20 chars

Implementation:
  - Use validation library
  - Custom validators
  - Unified error response
```

---

## 6. Security Design

### 6.1 Authentication & Authorization

```yaml
Authentication:
  - JWT token
  - Token expiry: 7 days
  - Refresh token supported

Authorization:
  - RBAC model
  - API-level permission control
  - Data-level permission control
```

### 6.2 Data Encryption

```yaml
Transmission:
  - HTTPS protocol
  - TLS 1.2+

Storage:
  - Password: bcrypt
  - Sensitive data: AES
  - Config: Environment variables

Key management:
  - Key rotation
  - No hardcoding
```

### 6.3 Security Protection

```yaml
SQL Injection:
  - Parameterized queries
  - ORM framework

XSS:
  - Output encoding
  - CSP policy

CSRF:
  - CSRF token
  - SameSite cookie

DDoS:
  - Rate limiting: 100 req/min/IP
  - CAPTCHA
  - IP blacklist
```

---

## 7. Performance Optimization

### 7.1 Caching Strategy

```yaml
Cache types:
  - Data cache: Redis
  - Query cache: Database
  - Page cache: Not applicable (API)

Cache scenarios:
  - User info: 1 hour
  - Config data: 24 hours
  - Hot data: 10 minutes

Cache update:
  - Active: On data change
  - Passive: On expiry
  - Scheduled: Hourly

Cache issues:
  - Penetration: Bloom filter
  - Breakdown: Randomized expiry
  - Avalanche: Expiry jitter
```

### 7.2 Database Optimization

```yaml
Query optimization:
  - Use indexes
  - Avoid SELECT *
  - Pagination
  - Slow query log

Connection pool:
  - Max: 100
  - Min: 10
  - Timeout: 30s
  - Idle timeout: 300s

Read-write split:
  - Master: Writes
  - Slaves: Reads
  - Middleware: ProxySQL
```

### 7.3 API Optimization

```yaml
Response optimization:
  - Compression: gzip
  - Reduce payload
  - Pagination

Concurrency:
  - Connection pooling
  - Async processing
  - Queue for peak loads

Rate limiting:
  - Token bucket
  - Leaky bucket
  - Sliding window
```

---

## 8. Deployment & Operations

### 8.1 Environment Configuration

```yaml
Development:
  - Node.js: 18.x
  - PostgreSQL: 14.x
  - Redis: 6.x

Production:
  - Node.js: 18.x LTS
  - PostgreSQL: 14.x
  - Redis: 6.x
  - Nginx: 1.24.x
```

### 8.2 Deployment Strategy

```yaml
Architecture:
  - Load balancer: Nginx
  - App server: PM2 / K8s
  - Database: Master-slave

Process:
  1. Build image
  2. Push image
  3. Update deployment
  4. Health check
  5. Rollback if needed

CI/CD:
  - Auto test
  - Auto build
  - Auto deploy
```

### 8.3 Monitoring & Alerting

```yaml
Metrics:
  - System: CPU, memory, disk
  - Application: QPS, latency, errors
  - Business: Orders, users

Tools:
  - Prometheus: Collection
  - Grafana: Visualization
  - AlertManager: Alerts

Alert rules:
  - CPU > 80%
  - Memory > 80%
  - Error rate > 1%
  - Response time > 1s
```

### 8.4 Logging

```yaml
Log levels:
  - ERROR: Errors
  - WARN: Warnings
  - INFO: Information
  - DEBUG: Debug

Log content:
  - User actions
  - System errors
  - API requests
  - Performance data

Log management:
  - Filebeat: Collection
  - Logstash: Processing
  - Elasticsearch: Storage
  - Kibana: Query
```

---

## 9. Testing

### 9.1 Unit Tests

```yaml
Framework:
  - Node.js: Jest
  - Python: pytest
  - Java: JUnit

Coverage:
  - Code: > 80%
  - Branch: > 70%
```

### 9.2 Integration Tests

```yaml
Tools:
  - Postman
  - Supertest

Content:
  - API tests
  - DB integration
  - Cache integration
```

### 9.3 Load Tests

```yaml
Tools:
  - JMeter
  - Apache Bench
  - wrk

Metrics:
  - QPS: > 1000
  - Latency: < 100ms
  - Error rate: < 0.1%
```
