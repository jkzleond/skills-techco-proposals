# Frontend Technical Documentation Template

Template for frontend development technical documentation.

---

## Document Structure

```markdown
# [Project Name] Frontend Technical Documentation

## 1. Tech Stack
## 2. Project Structure
## 3. Development Standards
## 4. Component Design
## 5. State Management
## 6. Routing Design
## 7. API Integration
## 8. Styling Guidelines
## 9. Build & Deploy
```

---

## 1. Tech Stack

```yaml
Framework: Vue 3.x
Build Tool: Vite 4.x
Language: TypeScript 5.x
Package Manager: pnpm / npm
UI Framework: Element Plus 2.x
Styling: Tailwind CSS 3.x
State: Pinia 2.x
Router: Vue Router 4.x
HTTP: Axios 1.x
```

---

## 2. Project Structure

```
src/
├── assets/          # Static resources
├── components/      # Reusable components
│   ├── common/      # Generic components
│   └── business/    # Business components
├── composables/     # Composition functions
├── layouts/         # Layout components
├── pages/           # Page components
├── router/          # Route configuration
├── stores/          # State management
├── api/             # API modules
├── utils/           # Utility functions
├── types/           # TypeScript types
├── constants/       # Constants
├── App.vue
└── main.ts
```

---

## 3. Development Standards

### 3.1 Code Style

**Component template**:
```vue
<template>
  <!-- Template content -->
</template>

<script setup lang="ts">
// 1. Imports
import { ref, computed } from 'vue'

// 2. Props
interface Props {
  title: string
}
const props = defineProps<Props>()

// 3. Emits
const emit = defineEmits<{
  update: [value: string]
}>()

// 4. State
const data = ref<string>('')

// 5. Computed
const formatted = computed(() => data.value)

// 6. Methods
const handleClick = () => {}

// 7. Lifecycle
onMounted(() => {})
</script>

<style scoped lang="scss">
// Styles
</style>
```

**Naming conventions**:
- Components: PascalCase (UserList.vue)
- Functions: camelCase (getUserInfo)
- Constants: UPPER_SNAKE_CASE (API_BASE_URL)
- Types: PascalCase (UserInfo)

### 3.2 TypeScript Standards

```typescript
// Interface
interface User {
  id: number
  name: string
  email: string
}

// Generic function
function fetchData<T>(url: string): Promise<T> {
  return axios.get<T>(url).then(res => res.data)
}

// Type guard
function isUser(value: unknown): value is User {
  return typeof value === 'object' && value !== null && 'id' in value
}
```

---

## 4. Component Design

### 4.1 Component Categories

**Base Components**: Reusable UI components
- Button, Input, Select, etc.

**Business Components**: Domain-specific components
- UserCard, CustomerList, etc.

**Layout Components**: Page layout
- DefaultLayout, AuthLayout, etc.

### 4.2 Component Communication

**Props / Emits**:
```vue
<script setup lang="ts">
interface Props {
  data: DataType[]
}
const props = defineProps<Props>()

const emit = defineEmits<{
  update: [value: string]
}>()
</script>
```

**Provide / Inject**:
```typescript
// Parent
provide('theme', ref('dark'))

// Child
const theme = inject<Ref<string>>('theme')
```

**Slots**:
```vue
<template>
  <div>
    <slot name="header">Default header</slot>
    <slot></slot>
    <slot name="footer"></slot>
  </div>
</template>
```

---

## 5. State Management

### 5.1 Store Module

```typescript
import { defineStore } from 'pinia'

export const useUserStore = defineStore('user', () => {
  // State
  const token = ref<string>('')
  const userInfo = ref<User | null>(null)

  // Getters
  const isLoggedIn = computed(() => !!token.value)

  // Actions
  const setToken = (newToken: string) => {
    token.value = newToken
  }

  const logout = () => {
    token.value = ''
    userInfo.value = null
  }

  return {
    token,
    userInfo,
    isLoggedIn,
    setToken,
    logout
  }
})
```

### 5.2 Store Usage

```vue
<script setup lang="ts">
import { useUserStore } from '@/stores/modules/user'

const userStore = useUserStore()

// Read state
console.log(userStore.isLoggedIn)

// Call actions
userStore.setToken('xxx')
</script>
```

---

## 6. Routing Design

### 6.1 Route Configuration

```typescript
const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('@/layouts/DefaultLayout.vue'),
    children: [
      {
        path: 'home',
        name: 'Home',
        component: () => import('@/pages/home/index.vue'),
        meta: { title: '首页', requiresAuth: true }
      }
    ]
  }
]
```

### 6.2 Route Guards

```typescript
router.beforeEach((to, from, next) => {
  const userStore = useUserStore()

  document.title = `${to.meta.title} - App`

  if (to.meta.requiresAuth && !userStore.isLoggedIn) {
    next({ name: 'Login', query: { redirect: to.fullPath } })
  } else {
    next()
  }
})
```

---

## 7. API Integration

### 7.1 Axios Setup

```typescript
import axios from 'axios'

const service = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL,
  timeout: 15000
})

// Request interceptor
service.interceptors.request.use(
  (config) => {
    const token = useUserStore().token
    if (token) {
      config.headers.Authorization = `Bearer ${token}`
    }
    return config
  }
)

// Response interceptor
service.interceptors.response.use(
  (response) => response.data.data,
  (error) => {
    // Error handling
    return Promise.reject(error)
  }
)
```

### 7.2 API Module

```typescript
import request from '../request'

export function getUserInfo(): Promise<User> {
  return request({
    url: '/user/info',
    method: 'get'
  })
}

export function updateUser(data: Partial<User>): Promise<User> {
  return request({
    url: '/user/update',
    method: 'put',
    data
  })
}
```

---

## 8. Styling Guidelines

### 8.1 Tailwind Configuration

```javascript
export default {
  theme: {
    extend: {
      colors: {
        primary: '#409EFF',
        success: '#67C23A'
      }
    }
  }
}
```

### 8.2 SCSS Variables

```scss
// Colors
$primary-color: #409EFF;

// Spacing
$spacing-base: 16px;

// Typography
$font-size-base: 14px;
```

---

## 9. Build & Deploy

### 9.1 Environment Variables

```bash
# .env.development
VITE_API_BASE_URL=http://localhost:3000/api

# .env.production
VITE_API_BASE_URL=https://api.example.com
```

### 9.2 Build Commands

```json
{
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  }
}
```

### 9.3 Vite Config

```typescript
export default defineConfig({
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  server: {
    port: 3000,
    proxy: {
      '/api': 'http://localhost:8080'
    }
  }
})
```
