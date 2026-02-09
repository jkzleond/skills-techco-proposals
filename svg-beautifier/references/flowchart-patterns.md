## 🕸️ 逻辑流程图
- **卡片式节点**: 结合渐变与侧边装饰条。
```xml
<g filter="url(#shadow)">
  <rect x="0" y="0" width="200" height="60" rx="12" fill="url(#grad_bg)" stroke="#1890ff" stroke-width="1.5" />
  <rect x="10" y="15" width="4" height="30" rx="2" fill="#1890ff" />
</g>
```

## 🏗️ 系统架构图
- **分层容器**: 使用 `url(#layerGrad)`。
- **发光中枢**:
```xml
<g transform="translate(100, 200)" filter="url(#shadow)">
  <rect x="0" y="0" width="600" height="70" rx="35" fill="#1890ff" />
  <text x="300" y="45" text-anchor="middle" font-weight="bold" fill="#ffffff">核心中枢</text>
</g>
```
