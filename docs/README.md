<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-01
- 运行时间：2026-06-01 23:18:34 UTC
- 运行状态：成功
- 本次总论文数：15
- 精读区：8
- 速读区：7

### 今日简报（AI）
今日精读8篇、速读7篇三维视觉前沿论文，重点审视了多视图重建与多智能体SLAM的满分突破。
最值得关注的是循环Transformer实现无冗余多视图3D重建，以及协作式单目SLAM将先验学习引入户外多机系统。
建议读者优先追踪这两项工作的开源代码与实时应用，同时留意动态3D高斯场景图在长期理解中的潜力。
- 详情：[/202606/01/README](/202606/01/README)

### 精读区论文标签
1. [Déjà View: Looping Transformers for Multi-View 3D Reconstruction](/202606/01/2605.30215v2-dj-view-looping-transformers-for-multi-view-3d-reconstruction)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：使用循环Transformer进行多视图三维重建
2. [CoMo3R-SLAM: Collaborative Monocular Dense SLAM with Learned 3D Reconstruction Priors for Outdoor Multi-Agent Systems](/202606/01/2605.30488v1-como3r-slam-collaborative-monocular-dense-slam-with-learned-3d-reconstruction-priors-for-outdoor-multi-agent-systems)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：利用多视图学习三维重建先验的协作单目稠密SLAM
3. [Learning Global Motion with Compact Gaussians for Feed-Forward 4D Reconstruction](/202606/01/2605.31595v1-learning-global-motion-with-compact-gaussians-for-feed-forward-4d-reconstruction)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：基于紧凑3D高斯的单目视频前馈4D重建，实现动态场景重建
4. [$R^3$: 3D Reconstruction via Relative Regression](/202606/01/2605.26519v2-r3-3d-reconstruction-via-relative-regression)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：通过相对回归进行长上下文和流式三维重建
5. [DSD-GS: Dynamic-Static Decomposition of Gaussian Splatting for Efficient and High-Fidelity Dynamic Scene Reconstruction](/202606/01/2605.30863v1-dsd-gs-dynamic-static-decomposition-of-gaussian-splatting-for-efficient-and-high-fidelity-dynamic-scene-reconstruction)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：通过高斯泼溅的动静态分解进行动态场景重建
6. [VolFill: Single-View Amodal 3D Scene Reconstruction with Volumetric Flow Matching](/202606/01/2605.31466v1-volfill-single-view-amodal-3d-scene-reconstruction-with-volumetric-flow-matching)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：使用生成式体积流匹配从单张RGB图像重建完整场景几何，推断遮挡结构
7. [Feature-Optimized Vision for Adaptive 3D Scene Reconstruction](/202606/01/2605.31534v1-feature-optimized-vision-for-adaptive-3d-scene-reconstruction)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：自适应特征选择用于3D重建，通过评分特征以最大化有用轨迹，支持多视角立体
8. [RayDer: Scalable Self-Supervised Novel View Synthesis from Real-World Video](/202606/01/2605.31535v1-rayder-scalable-self-supervised-novel-view-synthesis-from-real-world-video)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从无约束视频中统一估计相机、重建场景并渲染以实现新视图合成

### 速读区论文标签
1. [DGSG-Mind: Dynamic 3D Gaussian Scene Graphs for Long-Term Scene Understanding and Grounding](/202606/01/2605.29879v2-dgsg-mind-dynamic-3d-gaussian-scene-graphs-for-long-term-scene-understanding-and-grounding)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：动态3D高斯场景图结合开放词汇语义，用于长期场景理解和接地，支持特征匹配。
2. [Geometry Matters: 3D Foundation Priors for Learning Semantic Correspondence](/202606/01/2605.30093v1-geometry-matters-3d-foundation-priors-for-learning-semantic-correspondence)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：利用3D基础模型先验改善跨图像语义对应，解决2D歧义
3. [Seeing Fast and Slow: Bimodal 3D Scene Graphs for Open-set Tasks](/202606/01/2605.31067v1-seeing-fast-and-slow-bimodal-3d-scene-graphs-for-open-set-tasks)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：生成粗粒度和细粒度双模态三维场景图以实现场景语义理解
4. [Topologically Consistent Multi-view 3D Head Reconstruction via Coarse-Guided Layered Surface Sampling](/202606/01/2605.31283v1-topologically-consistent-multi-view-3d-head-reconstruction-via-coarse-guided-layered-surface-sampling)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：从多视图图像重建具有密集语义对应的三维头部
5. [Triangle Splatting SLAM](/202606/01/2605.31419v1-triangle-splatting-slam)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：基于可微三棱化的密集RGB-D SLAM从姿态图像重建3D场景
6. [Category-Level 3D Correspondence in Camera Space via Morphable Object Priors](/202606/01/2605.28257v1-category-level-3d-correspondence-in-camera-space-via-morphable-object-priors)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：无需显式监督学习类别级三维对应，助力从图像理解三维物体
7. [GMOS: Grounding Moving Object Segmentation in 3D Space and Time](/202606/01/2605.30352v1-gmos-grounding-moving-object-segmentation-in-3d-space-and-time)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：从RGB视频进行3D感知的运动物体分割，与3D场景分割相关。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
