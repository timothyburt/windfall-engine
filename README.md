# ![Windfall Engine Banner](assets/banner.jpg)

## 🌬️ Windfall Engine
**The Multi-Modal Game Engine for Python.**

Windfall is a flexible, light-weight game engine designed to bridge the gap between retro terminal interfaces and modern graphical displays. Build your game logic once, and deploy it across three distinct modes.

[![License: MIT](https://img.shields.io/badge/License-MIT-teal.svg)](https://opensource.org/licenses/MIT)

## 📜 Project Status

| Version | History | Roadmap |
| :--- | :--- | :--- |
| ![Version](https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fraw.githubusercontent.com%2Ftimothyburt%2Fwindfall-engine%2Fmain%2Fupdates%2Fversion.json&query=%24.version&label=version&style=for-the-badge&color=blue) | [![History](https://img.shields.io/badge/Changelog-View_History-orange?style=for-the-badge&logo=gitbook&logoColor=white)](./CHANGELOG.md) | ![Roadmap](https://img.shields.io/badge/Roadmap-Phase_2:_Core-green?style=for-the-badge&logo=target) |

### 🚀 The Vision: One Core, Three Renderers
Windfall allows developers to focus on "The Brain" of their game while providing swappable "Eyes" for different platforms:

* **🕹️ TUI Mode:** High-performance terminal interface using `blessed`. Perfect for SSH-based games and minimalist roguelikes.
* **🎨 2D Mode:** Polished graphical experience powered by `pygame`.
* **⛰️ 3D Mode:** Immersive spatial environments (Godot/Panda3D Integration).

### 🛠️ Installation (Alpha)
Currently in development. You can install the core engine directly from GitHub:

```bash
pip install git+[https://github.com/timothyburt/windfall-engine.git](https://github.com/timothyburt/windfall-engine.git)