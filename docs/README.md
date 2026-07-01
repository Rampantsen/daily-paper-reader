<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-07-01
- 运行时间：2026-07-01 22:08:27 UTC
- 运行状态：成功
- 本次总论文数：15
- 精读区：8
- 速读区：7

### 今日简报（AI）
今日精读两篇高分论文《Ground4D》与《Occlusion-Robust Multi-Object Decoupling》，并速读三篇关于匹配、位姿估计和紧凑高斯泼溅的工作。
最值得关注的方向：单目视频的时序一致性4D重建，以及物理交互中如何鲁棒分离并操控遮挡中的多个物体。
建议继续追踪这两项技术的开源实验，尤其适合想在自己项目中实现视频转动态3D或机器人抓取的用户。
- 详情：[/202607/01/README](/202607/01/README)

### 精读区论文标签
1. [Ground4D: Consistency-Aware 4D Reconstruction from Monocular Video](/202607/01/2606.28828v1-ground4d-consistency-aware-4d-reconstruction-from-monocular-video)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：利用三维基础模型从单目视频进行四维重建以获得多视图一致性几何
2. [Occlusion-Robust Multi-Object Decoupling for Physics-Based Robotic Interaction](/202607/01/2606.29303v2-occlusion-robust-multi-object-decoupling-for-physics-based-robotic-interaction)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从稀疏遮挡视图进行无掩码多物体三维重建
3. [T2LDM++: A Self-Conditioned Representation Guided Diffusion Model for Realistic Text-to-LiDAR Scene Generation](/202607/01/2606.30147v1-t2ldm-a-self-conditioned-representation-guided-diffusion-model-for-realistic-text-to-lidar-scene-generation)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：使用自条件表示引导的扩散模型进行文本到LiDAR场景生成
4. [UnfoldArt: Zero-Shot Recovery of Full Articulated 3D Objects from Text or Image](/202607/01/2606.30608v2-unfoldart-zero-shot-recovery-of-full-articulated-3d-objects-from-text-or-image)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从文本或图像零样本重建铰接三维物体
5. [DANTE-W: Diffuse Albedo Neural Texturing in the Wild](/202607/01/2606.30677v1-dante-w-diffuse-albedo-neural-texturing-in-the-wild)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从无结构图像集合中恢复大规模场景的高保真纹理
6. [Streaming Gaussian Encoding for 4D Panoptic Occupancy Tracking](/202607/01/2606.30754v1-streaming-gaussian-encoding-for-4d-panoptic-occupancy-tracking)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：基于多视图图像的4D全景占用追踪，联合推理几何、语义和物体身份
7. [CasaMaestro: Multi-View Panoramas for House-Scale 3D Reconstruction](/202607/01/2606.31086v1-casamaestro-multi-view-panoramas-for-house-scale-3d-reconstruction)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：多视图全景图用于房屋级三维重建
8. [LiteMatch: Lightweight Zero-Shot Stereo Matching via Cost Volume Stabilization](/202607/01/2606.31636v1-litematch-lightweight-zero-shot-stereo-matching-via-cost-volume-stabilization)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：轻量级零样本立体匹配实现跨域鲁棒视差估计

### 速读区论文标签
1. [REDI-Match: Rotation-Equivariant Distillation for Efficient and Robust Dense Matching](/202607/01/2606.24330v2-redi-match-rotation-equivariant-distillation-for-efficient-and-robust-dense-matching)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：旋转等变密集匹配蒸馏，实现鲁棒多视图特征匹配
2. [Planar-SfM: Camera Pose Estimation via Homography Graph Embeddings](/202607/01/2606.31979v1-planar-sfm-camera-pose-estimation-via-homography-graph-embeddings)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：利用单应性分解为平面场景估计相机姿态，提升在极线几何退化场景中的鲁棒性
3. [PointSplat: Compact Gaussian Splatting via Human-Centric Prediction](/202607/01/2606.32036v1-pointsplat-compact-gaussian-splatting-via-human-centric-prediction)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：从多视图输入推断紧凑的三维人体表示
4. [Beyond 2D Matching: A Unified Single-Stage Framework for Geometry-Aware Cross-View Object Geo-Localization](/202607/01/2606.30576v1-beyond-2d-matching-a-unified-single-stage-framework-for-geometry-aware-cross-view-object-geo-localization)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：几何感知的跨视角物体匹配用于地理定位，利用相机姿态和多模态提示
5. [AnyMatch: Supercharging Universal Multi-Modal Image Matching with Large-Scale Single-View Images](/202607/01/2606.31077v1-anymatch-supercharging-universal-multi-modal-image-matching-with-large-scale-single-view-images)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：利用单视图图像生成多模态匹配数据，提升三维场景理解中的特征匹配
6. [NaLA: A 3D Native LLM Layout Agent for High-quality 3D Scene Generation](/202607/01/2606.29395v1-nala-a-3d-native-llm-layout-agent-for-high-quality-3d-scene-generation)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：三维原生大语言模型智能体通过放置资产生成三维场景
7. [Knowledge-Driven Dimension Estimation from a Single Image -3D Asset Generation Technology for Digital Twin Construction](/202607/01/2606.30896v1-knowledge-driven-dimension-estimation-from-a-single-image--3d-asset-generation-technology-for-digital-twin-construction)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：尺寸估计辅助3D资产生成


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
