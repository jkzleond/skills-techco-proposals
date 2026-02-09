# Vue3 + Tailwind + Element Plus Component Styles

Quick reference for generating prototype code.

---

## Element Plus Common Components

### Form Components

**Input**
```vue
<el-input v-model="formData.username" placeholder="请输入" clearable />
```

**Password**
```vue
<el-input v-model="formData.password" type="password" show-password />
```

**Button**
```vue
<el-button type="primary">主要按钮</el-button>
<el-button>次要按钮</el-button>
<el-button type="text">文字按钮</el-button>
```

**Select**
```vue
<el-select v-model="formData.role" placeholder="请选择">
  <el-option label="管理员" value="admin" />
  <el-option label="用户" value="user" />
</el-select>
```

### Data Components

**Table**
```vue
<el-table :data="tableData">
  <el-table-column prop="name" label="姓名" />
  <el-table-column prop="email" label="邮箱" />
</el-table>
```

**Card**
```vue
<el-card>
  <template #header>
    <span>卡片标题</span>
  </template>
  <div>卡片内容</div>
</el-card>
```

**Tag**
```vue
<el-tag type="success">成功</el-tag>
<el-tag type="warning">警告</el-tag>
```

---

## Tailwind Common Patterns

### Layout

**Flex center**
```html
<div class="flex justify-center items-center">
  <span>居中内容</span>
</div>
```

**Flex space between**
```html
<div class="flex justify-between">
  <span>左侧</span>
  <span>右侧</span>
</div>
```

**Grid 2 columns**
```html
<div class="grid grid-cols-2 gap-4">
  <div>列1</div>
  <div>列2</div>
</div>
```

### Spacing

**Padding**
```html
<div class="p-4">全方向内边距</div>
<div class="px-4 py-2">左右上下内边距</div>
```

**Margin**
```html
<div class="m-4">全方向外边距</div>
<div class="mb-4">下外边距</div>
```

### Typography

**Text size**
```html
<span class="text-sm">小文本</span>
<span class="text-base">正常文本</span>
<span class="text-lg">大文本</span>
<span class="text-xl">特大文本</span>
```

**Text weight**
```html
<span class="font-normal">正常</span>
<span class="font-medium">中等</span>
<span class="font-semibold">半粗</span>
<span class="font-bold">粗体</span>
```

---

## Common Layout Patterns

### Login Page

```vue
<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 to-indigo-100 flex justify-center items-center">
    <div class="bg-white p-8 rounded-lg shadow-lg w-full max-w-md">
      <h1 class="text-3xl font-bold text-center mb-8">登录</h1>
      <el-form :model="formData">
        <el-form-item>
          <el-input v-model="formData.username" placeholder="账号" />
        </el-form-item>
        <el-form-item>
          <el-input v-model="formData.password" type="password" placeholder="密码" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" class="w-full">登录</el-button>
        </el-form-item>
      </el-form>
    </div>
  </div>
</template>
```

### Admin Layout

```vue
<template>
  <div class="flex h-screen">
    <!-- Sidebar -->
    <div class="w-64 bg-gray-800 text-white">
      <div class="p-4 text-xl font-bold">系统管理</div>
      <el-menu background-color="#1f2937" text-color="#fff">
        <el-menu-item index="1">首页</el-menu-item>
        <el-menu-item index="2">用户管理</el-menu-item>
      </el-menu>
    </div>

    <!-- Main -->
    <div class="flex-1 bg-gray-100">
      <div class="bg-white p-4 shadow">
        <span class="text-xl font-semibold">页面标题</span>
      </div>
      <div class="p-6">
        <router-view />
      </div>
    </div>
  </div>
</template>
```

---

## Vue Router Setup

```javascript
const { createRouter, createWebHashHistory } = VueRouter;

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: LoginPage },
  { path: '/home', component: HomePage },
  { path: '/customers', component: CustomerList }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes
});

app.use(router);
```

---

## State Management (Reactive)

```javascript
const { createApp, ref, computed } = Vue;

setup() {
  const formData = ref({
    username: '',
    password: ''
  });

  const loading = ref(false);

  const handleSubmit = async () => {
    loading.value = true;
    // API call
    loading.value = false;
  };

  return {
    formData,
    loading,
    handleSubmit
  };
}
```

---

## CDN Links

```html
<script src="https://cdn.tailwindcss.com"></script>
<link rel="stylesheet" href="https://unpkg.com/element-plus/dist/index.css">
<script src="https://unpkg.com/vue@3"></script>
<script src="https://unpkg.com/element-plus"></script>
<script src="https://unpkg.com/vue-router@4"></script>
```
