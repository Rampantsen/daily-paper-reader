<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-06-06
- 运行时间：2026-06-06 20:32:31 UTC
- 运行状态：成功
- 本次总论文数：16
- 精读区：6
- 速读区：10

### 今日简报（AI）
今日精读两篇顶会高分论文，聚焦多模态大模型的空间推理突破与3D生成的对称性约束创新。  
最值得关注的是：用宽基线匹配迫使模型学会复杂空间关系推理，以及将数学对称性编码进体素潜变量来稳定3D形状生成。  
感兴趣的朋友可以顺着这两个方向，结合自己的应用场景尝试把空间先验或结构对称性植入生成模型，往往能带来意想不到的性能跃升。
- 详情：[/202606/06/README](/202606/06/README)

### 精读区论文标签
1. [Eliciting Complex Spatial Reasoning in MLLMs through Wide-Baseline Matching](/202606/06/2606.03577v1-eliciting-complex-spatial-reasoning-in-mllms-through-wide-baseline-matching)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：宽基线匹配基准，评估多模态大模型跨视角的细粒度对应关系。
2. [SymTRELLIS: Symmetry-Enforced Voxel Latents for 3D Generation](/202606/06/2606.04108v1-symtrellis-symmetry-enforced-voxel-latents-for-3d-generation)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：在基于流的单视图三维生成中强制点群对称性，无需重新训练基础模型。
3. [A Cookbook of 3D Vision: Data, Learning Paradigms, and Application](/202606/06/2606.04291v1-a-cookbook-of-3d-vision-data-learning-paradigms-and-application)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：提供涵盖三维场景重建、多视图立体视觉、三维生成与语义分割的分类体系，是组合三维视觉主题的核心综述。
4. [PersistGS: Differentiable Physics for Object Permanence in 4D Gaussian Splatting](/202606/06/2606.03479v1-persistgs-differentiable-physics-for-object-permanence-in-4d-gaussian-splatting)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：从多相机视频中重建动态场景，利用可微物理保持遮挡下的物体持久性。
5. [Recent Advances and Trends in Learning-based 3D Representations](/202606/06/2606.04871v1-recent-advances-and-trends-in-learning-based-3d-representations)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：综述涵盖三维重建、新视角合成、识别与生成等任务的三维表示。
6. [CIPER: A Unified Framework for Cross-view Image-retrieval and Pose-estimation](/202606/06/2606.05011v1-ciper-a-unified-framework-for-cross-view-image-retrieval-and-pose-estimation)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：统一跨视角特征匹配与位姿估计，用于大规模地理定位

### 速读区论文标签
1. [LiAuto-GeoX: Efficient Grounded Driving Transformer](/202606/06/2606.05774v1-liauto-geox-efficient-grounded-driving-transformer)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：面向自动驾驶的高效Transformer，从环视数据中进行密集3D重建，利用稀疏LiDAR先验。
2. [CamGeo: Sparse Camera-Conditioned Image-to-Video Generation with 3D Geometry Priors](/202606/06/2605.30895v2-camgeo-sparse-camera-conditioned-image-to-video-generation-with-3d-geometry-priors)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：蒸馏三维几何先验，实现稀疏相机姿态下几何一致的图像到视频生成。
3. [Non-Learning Low-Light Stereo Vision](/202606/06/2606.00379v1-non-learning-low-light-stereo-vision)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：从噪声图像进行立体视差估计，用于多视角立体三维重建
4. [Zero-Shot 3D Question Answering via Hierarchical View-to-Token Transportation](/202606/06/2606.03100v1-zero-shot-3d-question-answering-via-hierarchical-view-to-token-transportation)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：基于多视图选择的VLM零样本3D场景理解
5. [HOLA: Holistic Multi-Modal Alignment for Open-Set 3D Recognition](/202606/06/2606.01334v1-hola-holistic-multi-modal-alignment-for-open-set-3d-recognition)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：将三维物体与多视角对齐，有助于多视角特征匹配
6. [PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](/202606/06/2606.01649v1-physcene3d-physically-consistent-interactive-3d-tabletop-scene-generation)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：利用认知推理生成物理一致的三维桌面场景
7. [PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](/202606/06/2606.01649v2-physcene3d-physically-consistent-interactive-3d-tabletop-scene-generation)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：利用认知推理生成物理一致的三维桌面场景
8. [Honey, I Shrunk the Arc de Triomphe!](/202606/06/2606.02379v1-honey-i-shrunk-the-arc-de-triomphe)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：从互联网照片收集度量尺度数据集用于三维几何估计，助力无标签图像集合的三维重建。
9. [Global-Local Monte Carlo Tree Search in Vision-Language Models for Text-to-3D Indoor Scene Generation](/202606/06/2606.06002v1-global-local-monte-carlo-tree-search-in-vision-language-models-for-text-to-3d-indoor-scene-generation)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：利用蒙特卡洛树搜索进行文本到3D室内场景生成
10. [HomeWorld: A Unified Floorplan-to-Furnished Framework for Generating Controllable, Densely Interactive Whole-Home Scenes](/202606/06/2606.06390v1-homeworld-a-unified-floorplan-to-furnished-framework-for-generating-controllable-densely-interactive-whole-home-scenes)  
   标签：评分：6.0/10、query:d-gen-recon
   evidence：一个生成室内全屋三维场景的分层框架，属于三维场景生成范畴。


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
