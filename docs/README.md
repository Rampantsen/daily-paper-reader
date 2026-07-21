<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-07-21
- 运行时间：2026-07-21 21:49:02 UTC
- 运行状态：成功
- 本次总论文数：13
- 精读区：8
- 速读区：5

### 今日简报（AI）
今日聚焦3D高斯泼溅与单目几何：从拓扑平面重建、占用估计到底层几何先验的精读探索。
最值得关注的方向是TopoGS用拓扑感知优化结构化平面重建，以及RayOcc通过高斯混合提升遮挡场景的占用估计精度。
建议读者优先阅读两篇满分精读论文，并尝试将高斯泼溅的拓扑与占用思想结合到自己的单目重建任务中。
- 详情：[/202607/21/README](/202607/21/README)

### 精读区论文标签
1. [TopoGS: Planar Reconstruction via Topology-aware 3D Gaussian Splatting](/202607/21/2607.16838v1-topogs-planar-reconstruction-via-topology-aware-3d-gaussian-splatting)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：拓扑感知三维高斯泼溅实现从图像中连贯三维重建
2. [RayOcc: Occlusion-Aware Ray Occupancy Estimation via Gaussian Mixture Intensity](/202607/21/2607.17660v1-rayocc-occlusion-aware-ray-occupancy-estimation-via-gaussian-mixture-intensity)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：从多视图图像进行体素级语义占用预测并处理遮挡
3. [MuViSeg: Multi-View Segment Correspondences from Dense Geometry Priors](/202607/21/2607.17938v1-muviseg-multi-view-segment-correspondences-from-dense-geometry-priors)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：利用3D基础模型的密集几何先验学习多视图分割对应关系，在实例分割级别进行匹配，用于对象级建图。
4. [CSS-BA: Gate-Guided Column Space Search for Bundle Adjustment](/202607/21/2607.15652v1-css-ba-gate-guided-column-space-search-for-bundle-adjustment)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：捆绑调整在低视差情况下稳定多视图三维重建
5. [Scene-SAM3D: Multi-View Scene Asset Generation Without Fine-Tuning](/202607/21/2607.16805v1-scene-sam3d-multi-view-scene-asset-generation-without-fine-tuning)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：无需微调的多视图场景资产生成
6. [Splat-based 3D Scene Reconstruction with Extreme Motion-blur](/202607/21/2607.16926v1-splat-based-3d-scene-reconstruction-with-extreme-motion-blur)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：在极端运动模糊下从RGB-D进行三维场景重建，克服相机位姿失败
7. [Text2Villa: Hierarchical Generation of 3D Indoor Environments with Physics-Aware Analysis-by-Synthesis](/202607/21/2607.17145v1-text2villa-hierarchical-generation-of-3d-indoor-environments-with-physics-aware-analysis-by-synthesis)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从自然语言分层生成室内三维环境，并采用物理感知物品布置
8. [VGOcc: Learning Visual-Geometric Gaussians for Vision-Centric 3D Driving Occupancy Prediction](/202607/21/2607.18078v1-vgocc-learning-visual-geometric-gaussians-for-vision-centric-3d-driving-occupancy-prediction)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从环视图像恢复语义3D占用场

### 速读区论文标签
1. [MetaView: Monocular Novel View Synthesis with Scale-Aware Implicit Geometry Priors](/202607/21/2607.12000v1-metaview-monocular-novel-view-synthesis-with-scale-aware-implicit-geometry-priors)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：基于扩散的单目新视角合成，结合尺度感知隐式几何，实现大视角变化下的场景生成
2. [CDIS: Cross-Dimensional Class-Agnostic 3D Instance Segmentation via 2D Mask Tracking and 3D-2D Projection Merging](/202607/21/2607.17778v1-cdis-cross-dimensional-class-agnostic-3d-instance-segmentation-via-2d-mask-tracking-and-3d-2d-projection-merging)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：利用跨帧2D掩码跟踪实现类别无关的3D实例分割
3. [FoundationGeo: Learning Spatial Pixel-Wise Fields for Monocular Metric Geometry](/202607/21/2607.11588v2-foundationgeo-learning-spatial-pixel-wise-fields-for-monocular-metric-geometry)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：单目度量三维点云估计，逐像素标定用于三维重建
4. [Fine-Detail Monocular Geometry Estimation with Self-Guided Sparse Volumetric Refinement](/202607/21/2607.17967v1-fine-detail-monocular-geometry-estimation-with-self-guided-sparse-volumetric-refinement)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：单目几何估计从单张图像重建精细三维细节
5. [Robust Multimodal Dynamic Object Segmentation](/202607/21/2607.18153v1-robust-multimodal-dynamic-object-segmentation)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：通过多模态动态分割实现动态视频的静态场景重建


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
