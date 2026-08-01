<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-08-01
- 运行时间：2026-08-01 21:08:21 UTC
- 运行状态：成功
- 本次总论文数：14
- 精读区：6
- 速读区：8

### 今日简报（AI）
今日从14篇论文中精读2篇、速读3篇，聚焦3D重建与视觉生成。  
亮点是10分论文用卷积神经着色实现高质量多视图重建，9分工作则让路面重建学会理解道路拓扑。  
建议读者优先关注“渲染+重建”融合的新范式，并跟进轻量化立体深度估计中的高效Token混合思路。
- 详情：[/202608/01/README](/202608/01/README)

### 精读区论文标签
1. [Convolutional Neural Shading for High-Quality 3D Reconstruction from Multi-View Images](/202608/01/2607.28132v1-convolutional-neural-shading-for-high-quality-3d-reconstruction-from-multi-view-images)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：卷积神经着色实现多视角高质量三维重建
2. [RoadVGGT: Road-Structure-Aware Feed-Forward Road Surface Reconstruction](/202608/01/2607.23758v1-roadvggt-road-structure-aware-feed-forward-road-surface-reconstruction)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从多视角图像重建道路三维表面
3. [WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing](/202608/01/2607.25234v1-whtmix-efficient-stereo-depth-estimation-via-walsh-hadamard-token-mixing)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：用Walsh-Hadamard令牌混合替代自注意力实现高效立体深度估计
4. [4DHumanDiff: Direct Text-to-4DGS Generation for Consistent 360-Degree Dynamic Humans](/202608/01/2607.27634v1-4dhumandiff-direct-text-to-4dgs-generation-for-consistent-360-degree-dynamic-humans)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从文本直接生成动态人类的4D高斯泼溅
5. [Split and Drive: Dual-Axis Disentanglement for Real-Time Gaussian Head Avatars](/202608/01/2607.28032v1-split-and-drive-dual-axis-disentanglement-for-real-time-gaussian-head-avatars)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从单张图像生成逼真可驱动头部化身，使用3D高斯点云
6. [S-Avatar: Diffusion-Guided Gaussian Head Avatars from a Single Image](/202608/01/2607.28164v1-s-avatar-diffusion-guided-gaussian-head-avatars-from-a-single-image)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：从单张图像生成3D头部化身，符合从图像生成3D物体的需求。

### 速读区论文标签
1. [WHTMix: Efficient Stereo Depth Estimation via Walsh-Hadamard Token Mixing](/202608/01/2607.25234v2-whtmix-efficient-stereo-depth-estimation-via-walsh-hadamard-token-mixing)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：使用沃尔什-哈达玛令牌混合替代自注意力实现高效立体深度估计
2. [MonoVoc: Decoupling Geometry and Semantics for Lightweight Monocular Open-Vocabulary 3D Gaussians](/202608/01/2607.28300v1-monovoc-decoupling-geometry-and-semantics-for-lightweight-monocular-open-vocabulary-3d-gaussians)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：免训练管线解耦几何与语义，从单目视频实现开放词汇三维场景理解
3. [ROAD: Reciprocal-Objective Alignment of Discriminative Semantics for 3D Shape Generation](/202608/01/2607.28581v1-road-reciprocal-objective-alignment-of-discriminative-semantics-for-3d-shape-generation)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：将判别性三维基础模型先验迁移至扩散变换，实现高效三维形状生成
4. [Genie Sim PanoWorld: An Infinite Indoor 3D World Generation Pipeline via Panoramic Scene Modeling and Simulation](/202608/01/2607.26646v1-genie-sim-panoworld-an-infinite-indoor-3d-world-generation-pipeline-via-panoramic-scene-modeling-and-simulation)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：从单张全景图生成三维室内场景
5. [Articulated Object Reconstruction from Rest-State Observation](/202608/01/2607.27749v1-articulated-object-reconstruction-from-rest-state-observation)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：从单一图像重建3D铰接物体
6. [PlanCraft: Sketch, Refine, and Furnish for Architect-Inspired Progressive 3D Residential Scene Generation](/202608/01/2607.23491v1-plancraft-sketch-refine-and-furnish-for-architect-inspired-progressive-3d-residential-scene-generation)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：从草图出发通过草图、精炼、家具布置阶段渐进式生成3D住宅场景
7. [3DGBGS: 3D Granular Ball Gaussian Splatting for Compact Novel View Synthesis](/202608/01/2607.26578v1-3dgbgs-3d-granular-ball-gaussian-splatting-for-compact-novel-view-synthesis)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：通过颗粒球组织改进3DGS新视角合成，实现紧凑场景重建
8. [MeshFM: 2D Features Are All You Need for 3D Shape Understanding](/202608/01/2607.27592v1-meshfm-2d-features-are-all-you-need-for-3d-shape-understanding)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：从二维学习三维特征用于分割与对应


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
