# Blender-autosave-images-by-ctrl-s
Automatically saves unsaved images to a specified folder when saving the .blend file, avoids name conflicts, can save only unpacked images, and provides manual save buttons with numbered suffix.

# Auto Save Images with Blend / Blender 自动保存贴图插件

**Version / 版本:** 1.0.0  
**Blender Compatible / 适用 Blender 版本:** 4.0+  
**Author / 作者:** pp  
**License / 许可证:** GPL-3.0  

---

## Overview / 插件概述

**Auto Save Images with Blend** is a Blender add-on that automatically saves unsaved images when you save your `.blend` file. It also provides manual save buttons in the 3D View sidebar, allowing flexible control over your textures.

**Blender 自动保存贴图插件**可以在保存 `.blend` 文件时自动保存未保存的贴图，并在 3D 视图侧栏提供手动保存按钮，方便用户灵活管理贴图。

---

## Features / 功能

1. **Automatic Save on .blend Save / Ctrl+S 自动保存**
    
    - Saves unsaved images when you press Ctrl+S.
        
    - Option to save only unpacked images (ignores images with existing paths).
        
    - Ctrl+S 时自动保存未保存的贴图，可选择只保存未打包的贴图。
        
2. **Manual Save Buttons in Sidebar / 手动保存按钮**
    
    - **Save All Modified Images:** calls `bpy.ops.image.save_all_modified()`.
        
        - 保存所有修改过的贴图（调用 Blender 原生命令）。
            
    - **Save Unpacked Images Now:** manually save images without file paths to the configured folder.
        
        - 手动保存无路径贴图到指定文件夹。
            
    - **Save All Images Numbered (Suffix):** saves images using their original names plus a numbered suffix (e.g., `Texture.001.png`, `Texture.002.png`), avoiding overwriting existing files.
        
        - 按原名加序号后缀保存贴图（如 `Texture.001.png`），避免覆盖已有文件。
            
3. **Custom Save Settings / 自定义保存设置**
    
    - Choose save format: PNG, JPEG, or EXR.
        
    - Set custom save directory (relative to `.blend` by default).
        
    - Automatically avoids name conflicts.
        
    - 支持选择保存格式（PNG/JPEG/EXR）、自定义保存目录（默认相对于 `.blend` 文件夹），自动避免文件名冲突。
        

---

## Installation / 安装方法

1. Download the latest release `.zip` file from GitHub.  
    从 GitHub 下载插件 `.zip` 文件。
    
2. In Blender: `Edit > Preferences > Add-ons > Install…`  
    在 Blender 中打开：`编辑 > 首选项 > 插件 > 安装…`
    
3. Select the downloaded `.zip` file and enable the add-on.  
    选择下载的 `.zip` 文件并启用插件。
    
4. You will find the panel in **3D View > Sidebar > AutoSave**.  
    插件面板位于 **3D 视图 > 侧栏 > AutoSave**。
    

---

## Usage / 使用方法

1. **Automatic Save / 自动保存:**
    
    - Enable "Enable Auto Save" in the sidebar.
        
    - Press Ctrl+S to automatically save unsaved or unpacked images.
        
    - 在侧栏勾选 “Enable Auto Save”，按 Ctrl+S 自动保存未保存或未打包的贴图。
        
2. **Manual Buttons / 手动按钮:**
    
    - **Save All Modified Images:** Save all currently modified images.
        
    - **Save Unpacked Images Now:** Save all images without existing file paths to the configured folder.
        
    - **Save All Images Numbered (Suffix):** Save all images to the folder using original names plus `.001`, `.002` suffix, avoiding overwrites.
        
    - 保存所有修改贴图 / 手动保存无路径贴图 / 按原名加序号后缀保存贴图
        
3. **Settings / 设置:**
    
    - Configure **Save Format**, **Save Directory**, and whether to **Only Save Unpacked Images** in the sidebar.
        
    - 在侧栏配置保存格式、保存目录以及是否仅保存未打包贴图。
        

---

## Example Workflow / 使用示例

1. Create textures in Blender or paint directly in Image Editor.  
    在 Blender 中创建贴图或直接在图像编辑器绘制贴图。
    
2. Keep images unpacked or newly created.  
    保持贴图未打包或新建。
    
3. Press Ctrl+S — all unsaved images are automatically saved in your specified folder.  
    按 Ctrl+S，所有未保存的贴图会自动保存到指定文件夹。
    
4. Use **Save All Images Numbered (Suffix)** to export all textures for backup or project sharing.  
    使用 “Save All Images Numbered (Suffix)” 按钮导出贴图备份或共享。
    

---

## Support & Contribution / 支持与贡献

- Please report issues or feature requests on the [GitHub Issues page](https://github.com/yourname/auto_save_images/issues).  
    在 [GitHub Issues](https://github.com/yourname/auto_save_images/issues) 提交问题或功能需求。
    
- Contributions are welcome! Fork the repository, make your changes, and submit a pull request.  
    欢迎贡献！Fork 仓库、修改代码并提交 Pull Request。
    

---

## License / 许可证

This add-on is licensed under **GPL-3.0**.  
本插件使用 **GPL-3.0** 协议，允许自由使用、修改和分发。
