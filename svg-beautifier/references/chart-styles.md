## 📊 柱状图 (Bar Charts)
- **轨道设计**: `rect` 作为轨道背景，填充色通常为 `#f0f0f0`。
- **代码参考**:
```xml
<rect x="100" y="50" width="400" height="12" rx="6" fill="#f0f0f0" />
<rect x="100" y="50" width="280" height="12" rx="6" fill="url(#grad_primary)" />
```

## 📈 折线图 (Line Charts)
- **贝塞尔曲线**: 路径必须平滑。
- **代码参考**:
```xml
<path d="M 50 200 C 150 150, 250 250, 350 100" fill="none" stroke="#1890ff" stroke-width="3" />
<path d="M 50 200 C 150 150, 250 250, 350 100 V 300 H 50 Z" fill="url(#area_grad)" opacity="0.2" />
```

## 🍰 饼图 (Pie Charts)
- **强调色**: 关键扇区应有轻微的偏移 (`transform="translate(...)"`) 或对比色。
