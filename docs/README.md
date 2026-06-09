<div class="dpr-home-notice-card">
  <h3 class="dpr-home-notice-title">🚀 Start Here</h3>
  <ul class="dpr-home-notice-list">
    <li><a href="#/tutorial/README">使用教程</a></li>
  </ul>
</div>

## 每次日报
- 最新运行日期：2026-05-31 ~ 2026-06-09
- 运行时间：2026-06-09 07:59:54 UTC
- 运行状态：成功
- 本次总论文数：15
- 精读区：7
- 速读区：8

### 今日简报（AI）
今日精读S23DR冠军方案与EPS3D全景分割，速览了SCOUT覆盖探索、卫星赋能尺度重建和CP4D物理感知4D生成。  
最具看点的方向是端到端3D感知（EPS3D）与重建模型借助卫星图获得真实尺度的突破。  
想上手实践，建议从EPS3D的feed-forward全景管线入手，搭配卫星先验赋予普通重建以米级精度。
- 详情：[/20260531-20260609/README](/20260531-20260609/README)

### 精读区论文标签
1. [S23DR 2026 Winning Solution](/20260531-20260609/2606.06695v1-s23dr-2026-winning-solution)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：从稀疏运动恢复结构、深度和语义分割进行三维线框重建
2. [EPS3D: End-to-End Feed-Forward 3D Panoptic Segmentation](/20260531-20260609/2606.08980v1-eps3d-end-to-end-feed-forward-3d-panoptic-segmentation)  
   标签：评分：10.0/10、query:d-gen-recon
   evidence：从多视图图像进行开放词汇三维全景分割
3. [ForestMamba: Sparse Mamba with Geometry-guided Queries for 3D Forest Point Cloud Segmentation](/20260531-20260609/2606.01549v1-forestmamba-sparse-mamba-with-geometry-guided-queries-for-3d-forest-point-cloud-segmentation)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：三维森林场景的点云语义和实例分割
4. [GVC-Seg: Training-Free 3D Instance Segmentation via Geometric Visual Correspondence](/20260531-20260609/2606.08014v1-gvc-seg-training-free-3d-instance-segmentation-via-geometric-visual-correspondence)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：提出基于几何视觉对应的免训练3D实例分割，解决基础模型聚合中的偏差问题。
5. [Rethinking 3D Shape Generation: Diffusion over Superquadrics](/20260531-20260609/2606.08957v1-rethinking-3d-shape-generation-diffusion-over-superquadrics)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：提出基于超二次曲面的扩散模型进行高效三维形状生成，直接处理三维物体生成
6. [See More, Match Better: Multi-Source Feature Fusion for Two-View Correspondence Learning](/20260531-20260609/2606.09262v1-see-more-match-better-multi-source-feature-fusion-for-two-view-correspondence-learning)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：提出多源特征融合改善两视图对应关系，直接处理多视图特征匹配
7. [EditSSC: Toward Editable Semantic Occupancy Scenes with Unconditional Diffusion Models](/20260531-20260609/2606.09273v1-editssc-toward-editable-semantic-occupancy-scenes-with-unconditional-diffusion-models)  
   标签：评分：9.0/10、query:d-gen-recon
   evidence：提出利用2D BEV和扩散模型进行3D语义场景生成，直接生成可编辑的3D占位场景。

### 速读区论文标签
1. [SCOUT: Semantic scene COverage via Uncertainty-guided Traversal](/20260531-20260609/2606.06721v1-scout-semantic-scene-coverage-via-uncertainty-guided-traversal)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：从RGB-D在线构建带语义标签的三维场景图谱
2. [Empowering Feed-Forward Reconstruction Models with Metric Scale via Satellite Images](/20260531-20260609/2606.08205v1-empowering-feed-forward-reconstruction-models-with-metric-scale-via-satellite-images)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：卫星图像引导的度量尺度三维重建
3. [CP4D: Compositional Physics-aware 4D Scene Generation](/20260531-20260609/2606.09187v1-cp4d-compositional-physics-aware-4d-scene-generation)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：带物理的动态三维场景生成
4. [HDSL: A Hierarchical Domain-Specific Language for Structured 3D Indoor Scene Generation and Localized Editing with LLM Agents](/20260531-20260609/2606.09738v1-hdsl-a-hierarchical-domain-specific-language-for-structured-3d-indoor-scene-generation-and-localized-editing-with-llm-agents)  
   标签：评分：8.0/10、query:d-gen-recon
   evidence：文本驱动的三维室内场景生成与编辑
5. [PhyScene3D: Physically Consistent Interactive 3D Tabletop Scene Generation](/20260531-20260609/2606.01649v1-physcene3d-physically-consistent-interactive-3d-tabletop-scene-generation)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：物理一致的三维桌面场景生成
6. [Hierarchical Space Partition for Surface Reconstruction](/20260531-20260609/2606.04891v1-hierarchical-space-partition-for-surface-reconstruction)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：利用平面组装从点云重建表面，与三维场景重建直接相关
7. [SceneConductor: 3D Scene Generation from Single Image with Multi-Agent Orchestration](/20260531-20260609/2606.08402v1-sceneconductor-3d-scene-generation-from-single-image-with-multi-agent-orchestration)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：从单张图像生成完整的3D场景
8. [PhysGraph: A Physics-aware 3D Scene Graph for Perception and Reasoning](/20260531-20260609/2606.08655v1-physgraph-a-physics-aware-3d-scene-graph-for-perception-and-reasoning)  
   标签：评分：7.0/10、query:d-gen-recon
   evidence：从RGB-D观测重建带物理和运动属性的物体级三维场景


<div class="dpr-home-promo-card">
  <h3 class="dpr-home-promo-title">💬 社区与支持</h3>
  <ul class="dpr-home-promo-list">
    <li>欢迎 Star / Fork / Issue / PR</li>
    <li>QQ群：583867967（欢迎交流，已有：1151人）</li>
  </ul>
</div>
