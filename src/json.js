const fs = require('fs');
const http = require('http');
const port = 3021;
const data = [
  {
      "id": 3459594,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 2241630,
      "pageTotal": 27,
      "title": "智明达（688636）：军用嵌入式计算机小巨人",
      "authors": "李聪,朱雨时",
      "orgName": "华泰证券",
      "orgIds": [
          9471
      ],
      "publishAt": "2023-03-16T12:35:47.000Z",
      "uploaderName": "范姜冰菱",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/49287b1cce707fc38f4eed5f7ce6682e2f8a525e.png",
      "stockName": "智明达",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "智明达（688636）：<em>军用</em>嵌入式计算机小巨人"
          ],
          "content": [
              "<em>军用</em>嵌入式计算机作为应用于\n军事领域的嵌入式计算机系统，它除了具有嵌入式计算机的普遍特性外，还具备可靠性高、\n环境适应性强、寿命保障性要求高等<em>军用</em>产品特点，因此从事<em>军用</em>嵌入式计算机的厂商大\n多都有多年从事军工相关产品研制生产的经验",
              "环境适应性强 武器装备往往处于恶劣应用环境中，因此<em>军用</em>嵌入式计算机须具有在高温、低温、冲击、震动、沙尘、霉菌、\n盐雾等恶劣环境下工作的能力 \n电磁兼容性 <em>军用</em>嵌入式计算机需符合电磁兼容国家<em>军用</em>标准的要求",
              "该产品在设计时采用通用化、\n系列化设计，可广泛用于各类激光惯组系统中 \n导引头 接口控制 \n \n<em>伺服</em>控制器 \n该产品为红外制导导引头的<em>伺服</em>控制和数据通信的核心部件，主要功能是通过专用总线与\n综合控制计算机进行通信",
              "该产品在设计时采用通用化、系列化设计，因此该产品可广泛用于各类导弹\n<em>伺服</em>控制系统中 \n信号处理 \n \n通用接口模块 \n该产品用于弹载雷达制导系统中，对数字化后的雷达回波信号进行数字信号处理，进一步\n对目标的距离和速度信息进行计算",
              "3）车载：公司的车载嵌入式计算机模块产品主要应用于车载武器电子信息系统中，主要包\n括：<em>伺服</em>控制，观瞄仪，综合管理，发射控制，显控装置等，这些装置主要用于实现侦察\n及武器发射等功能。"
          ]
      },
      "score": 24.3789
  },
  {
      "id": 3415706,
      "typeId": 14,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 3388444,
      "pageTotal": 25,
      "title": "运动控制系统：专用控制器应用面较广，伺服系统国产化率持续提升",
      "authors": "诸海滨,赵昊",
      "orgName": "开源证券",
      "orgIds": [
          9684
      ],
      "publishAt": "2023-01-20T03:14:51.000Z",
      "uploaderName": "Aaron",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/f207ed8e096486bf94e1473dda8219a1a2a81258.png",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "运动控制系统：专用控制器应用面较广，<em>伺服</em>系统国产化率持续提升"
          ],
          "content": [
              " 步进系统市场以内资品牌为主，<em>伺服</em>系统国产化率升至43%，替代空间广阔\n步进系统由步进电机和步进驱动器构成；<em>伺服</em>系统包括<em>伺服</em>驱动器、<em>伺服</em>电机、\n编码器三个部分。",
              "结构上，<em>伺服</em>系统（或称<em>伺服</em>产品）通常包\n括<em>伺服</em>驱动器（指令装置）、<em>伺服</em>电机、<em>伺服</em>反馈装置（编码器）三个部分，但通常\n<em>伺服</em>反馈装置（编码器）嵌入<em>伺服</em>电机之中。",
              "图：<em>伺服</em>系统主要由<em>伺服</em>驱动器、<em>伺服</em>电机和编码器组成\n\n资料来源：禾川科技招股书\n<em>伺服</em>电机（servo motor）是指在<em>伺服</em>系统中控制机械元件运转的发动机，是一\n种补助马达间接变速装置。",
              "图：<em>伺服</em>电机是一种补助马达间接变速装置\n\n图：闭环<em>伺服</em>机构中<em>伺服</em>电机接受脉冲信号运转\n\n\n\n资料来源：鸣志电器官网资料来源：同心智造网、开源证券研究所\n<em>伺服</em>电机有直流和交流<em>伺服</em>电动机之分，高性能的<em>伺服</em>系统大多采用永磁同步",
              "具备承担军工产品科研生产的相关资质，拥有<em>伺服</em>及控制领域优秀的科研技术人才，\n建立了完善的研发管理体系和质量管理体系，是国内领先的<em>军用</em>随动控制总成和军\n品级<em>伺服</em>系统提供商，也是国内较早从事<em>军用</em><em>伺服</em>系统产品研发与产业化的企业"
          ]
      },
      "score": 23.706347
  },
  {
      "id": 3417498,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1318318,
      "pageTotal": 29,
      "title": "振华风光（688439）：军用运算放大器领先企业，转型IDM模式强化企业护城河",
      "authors": "王天一,罗楠,冯函,丁昊",
      "orgName": "东方证券",
      "orgIds": [
          9134
      ],
      "publishAt": "2023-01-30T01:47:05.000Z",
      "uploaderName": "京城巧春",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/d3a55b59b90133511e031d56cb37df8132e929ad.png",
      "stockName": "振华风光",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "振华风光（688439）：<em>军用</em>运算放大器领先企业，转型IDM模式强化企业护城河"
          ],
          "content": [
              "5 \n1、<em>军用</em>运算放大器领先企业，业绩迈入高增通道 \n1.1 深耕<em>军用</em>模拟集成电路，高可靠运算放大器核心供应商 \n<em>军用</em>运算放大器国产化领军者，是国内高可靠运算放大器核心供应商。",
              "链产\n品 \n放大\n器 \n运算放大器 \n在模拟信号的传输过\n程中对信号进行放大\n等运算处理，可将微\n弱的电信号在不失真\n的前提下调节放大 \n运载火箭、飞\n机、导弹、装\n甲车、平台、\n通讯等 \n信号处理、<em>伺服</em>",
              "6 \nSiP集成电路 \n\\ \n运载火箭、导\n弹、飞机 \n功率驱动、<em>伺服</em>\n系统、陀螺、舵\n机等 \n系统封装具有体积小、集成\n度高、可靠性好、工作电压\n高、输出电流大、外壳与内\n部电路隔离等 \n轴角转换器",
              "9 \n \n2、<em>军用</em>模拟集成电路壁垒高，下游需求驱动市场增长 \n2.1 模拟集成电路链接虚实，<em>军用</em>高可靠度模拟IC壁垒高 \n集成电路：工业粮食，下游应用领域广泛。",
              "fA 级超低漏电流设计技术、\n±35KV ESD 的接口电路设计技术、高压大功率驱动器件布局布线技术、基于SOC的高压大功率驱\n动技术 \n机载、弹载、车\n载、舰载 \n系统封装集成\n电路 \n21 \n高阶<em>伺服</em>系统设计技术"
          ]
      },
      "score": 23.33493
  },
  {
      "id": 3505811,
      "typeId": 16,
      "businessId": 4,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1759789,
      "pageTotal": 20,
      "title": "晟楠科技（837006）北交所新股申购报告：军用航空部件及电源供应商，受益于换代需求",
      "authors": "诸海滨",
      "orgName": "开源证券",
      "orgIds": [
          9684
      ],
      "publishAt": "2023-04-16T15:15:18.000Z",
      "uploaderName": "濮阳心诺",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/9dd834fdcf07e2140c4aaa626c39ac920d9d18c6.png",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "晟楠科技（837006）北交所新股申购报告：<em>军用</em>航空部件及电源供应商，受益于换代需求"
          ],
          "content": [
              "，受益于换代需求\n——北交所新股申购报告\n\n\n\n诸海滨（分析师）\n\n证书编号：\n\n\n <em>军用</em>航空部件及电源供应商，年实现业绩万元（）\n晟楠科技成立于年，主要从事航空装备制造、<em>军用</em>电源领域相关产品研发\n生产与销售",
              "晟楠科技主要从事航空装备制造、<em>军用</em>电源领域相关产品的研发、生产和销售。",
              "此外还包括天馈<em>伺服</em>系统等产品。",
              "天馈<em>伺服</em>系\n统\n自动天馈<em>伺服</em>系统，通过机电控制及馈线自动\n收放，减少人工干预，实现车载各型高架天线\n的快速展开、撤收及天馈线的收藏，并解决电\n动升降杆手动架设多天线时人工作业时间较\n长的问题。",
              "根据《》数据，美国、\n俄罗斯、我国<em>军用</em>直升机数量分别为台、台、台，世界占比分别为、\n、，我国<em>军用</em>直升机数量不及美国的，差距明显，需求空间较大。"
          ]
      },
      "score": 23.209036
  },
  {
      "id": 3342614,
      "typeId": 10,
      "businessId": 9,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1728720,
      "pageTotal": 17,
      "title": "军工电子行业深度报告：海空强军需求驱动军用雷达换代列装",
      "authors": "贺潇翔宇",
      "orgName": "川财证券",
      "orgIds": [
          9634
      ],
      "publishAt": "2022-10-27T11:29:04.000Z",
      "uploaderName": "英彦少爷",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/ba6afd61418ea4af90f8465238625beef6433f18.png",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "军工电子行业深度报告：海空强军需求驱动<em>军用</em>雷达换代列装"
          ],
          "content": [
              "<em>军用</em>雷达包含多种元器件，T/R芯片及组件是关键部分。<em>军用</em>雷达由信号处理机、<em>伺服</em>\n机、频率定时器、双工器、T/R组件等构成，其中T/R组件的成本占比超50%。",
              "表 1：  军工电子分类 \n \n资料来源：前瞻产业研究院，川财证券研究所 \n<em>军用</em>雷达经历了二战、冷战等阶段的改进升级后，其<em>军用</em>性能已愈发强大。",
              "按工作\n频段的不同，<em>军用</em>雷达可分为米波雷达、分米波雷达、厘米波雷达、毫米波雷达等。按\n发射信号形式的不同，<em>军用</em>雷达可分为脉冲雷达、连续波雷达、脉冲压缩雷达等。",
              "12/17 \n信号处理机、<em>伺服</em>机、频率定时器、双工器、T/R组件等构成，其中T/R组件在有源相控\n阵雷达成本中的占比达50%以上。",
              "在<em>军用</em>领域，国\n博电子长期为陆、海、空、天等各型装备配套大量关键产品，确保了以T/R 组件为代表\n的关键<em>军用</em>元器件的国产自主化。"
          ]
      },
      "score": 22.499588
  },
  {
      "id": 3481732,
      "typeId": 10,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1416924,
      "pageTotal": 13,
      "title": "人工智能军用潜力大，自主武器和侦察指控等应用或成趋势",
      "authors": "杨晨",
      "orgName": "国金证券",
      "orgIds": [
          9551
      ],
      "publishAt": "2023-03-26T02:42:55.000Z",
      "uploaderName": "幕诗缱绻",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/0babea1dd98d6e1a5d06f961fd3393cbfd8ebf6f.png",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "人工智能<em>军用</em>潜力大，自主武器和侦察指控等应用或成趋势"
          ],
          "content": [
              "敬请参阅最后一页特别声明 \n1 \n  \n \n \n \n \n \n \n \n人工智能致力于构造具有智慧能力的系统，在<em>军用</em>领域有着多重应用价值。",
              "人工智能致力于研究人类智能行为规律、\n构造具有智慧能力的系统并做出有效反应和行动，在<em>军用</em>领域有着多重优势。",
              " 建议关注：航发高弹性标的航宇科技，航空锻铸造龙头中航重机，<em>军用</em>元器件一体化平台振华科技，高端无人机\n产业化核心平台中无人机，运输机和战略威慑机型唯一上市平台中航西飞。",
              "人工智能在<em>军用</em>领域有着多重优\n势，包括辅助决策支持及缓解人力紧缺问题等。",
              "人工智能可分为基础层、技术层、应用层，基础层是人工智能产业的基础，主要是包括芯片、传感控制\n等硬件设施及云计算等服务平台，提供数据服务和算力支撑，相关标的有集成电路供应商紫光国微、复旦微电、景嘉\n微等，以及<em>伺服</em>类产品厂商振华科技"
          ]
      },
      "score": 22.33665
  },
  {
      "id": 3518329,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 2350214,
      "pageTotal": 29,
      "title": "振华风光（688439）：军用模拟芯片龙头，发展动能强劲",
      "authors": "李聪,朱雨时",
      "orgName": "华泰证券",
      "orgIds": [
          9471
      ],
      "publishAt": "2023-04-24T13:23:06.000Z",
      "uploaderName": "Lian",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/362c40dd80c14f14cfae72daf0621324b51eb3ce.png",
      "stockName": "振华风光",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "振华风光（688439）：<em>军用</em>模拟芯片龙头，发展动能强劲"
          ],
          "content": [
              "(人民币): 141.60 \n \n2023年4月24日│中国内地 其他军工 \n \n \n<em>军用</em>模拟芯片龙头，首次覆盖给予“买入”评级 \n公司主营业务为<em>军用</em>模拟芯片研发生产，自产产品业务板块可分为信号链与\n电源管理器",
              "4 \n振华风光 (688439 CH) \n老牌<em>军用</em>集成电路企业进入快速发展期 \n“三线建设”时期重点IC企业，50余年打造<em>军用</em>模拟芯片旗舰企业 \n“三线建设”重点单位之一，国内老牌<em>军用</em>集成电路企业。",
              "立足放大器，持续开发新产品拓展业务条线，打造<em>军用</em>综合模拟芯片旗舰企业。",
              "可应用于武器装备中模拟前\n端、功率放大、各种传感器信\n号调理、<em>伺服</em>控制等场景。",
              "主要<em>军用</em>产品包括线性产品、转换器产\n品和接口等。"
          ]
      },
      "score": 22.28236
  },
  {
      "id": 3334823,
      "typeId": 10,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 4393221,
      "pageTotal": 23,
      "title": "军用雷达产业深度报告：国防信息之魂，现代战争之眼",
      "authors": "魏永",
      "orgName": "中航证券",
      "orgIds": [
          9306
      ],
      "publishAt": "2022-10-19T02:10:11.000Z",
      "uploaderName": "阿德拉姆",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/6e2895e924340c652a922d7eab84c1a21f9b9620.png",
      "stockName": null,
      "isHorizontal": true,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "<em>军用</em>雷达产业深度报告：国防信息之魂，现代战争之眼"
          ],
          "content": [
              "邮箱：weiy@avicsec.com\n\n引言——<em>军用</em>雷达：国防信息化重要组成，攻防兼备电子之眼\n2\n<em>军用</em>雷达的概念、分类、作用\n资料来源：《<em>军用</em>雷达技术在现代战争中的应用》、中航证券研究所\n<em>军用</em>雷达是用于军事目标的雷达",
              "的雷达发射机；向空间辐射信号和接收从目标反射信号的天线；将微弱的接收信号进行放大滤波和变换的雷达接收机；对雷达信号进行处理、录取与显示的雷达终端设备；\n控制雷达天线转动，控制与录取天线波束指向数据的雷达<em>伺服</em>设备",
              "简化的雷达组成方框图雷达工作原理\n发射/接收天线\n<em>伺服</em>设备\n雷达发射机\n频率综合器与定时器\n终端设备\n双工器\n雷达接收机\n信号处理机\n典型雷达基本组成\n天线发射机双工器电磁波目标\n电磁波发射过程\n天线接收机双工器回波目标",
              "<em>军用</em>雷达的重要性主要表现在三个方面：①<em>军用</em>雷达是各级别作战指挥系统中能够实时、主动、全天候获取有关\n目标战场环境信息的探测手段；②<em>军用</em>雷达是各类先进作战平台不可或缺的组成部分，是实现远程打击、精确打击的必要手段",
              "<em>军用</em>雷达最重要且技术水平最高的应用领域是机载雷达，机载雷达的技术升级牵引着<em>军用</em>雷达的性能和技术体制的持续\n创新。"
          ]
      },
      "score": 22.025877
  },
  {
      "id": 3412700,
      "typeId": 10,
      "businessId": 4,
      "labelIds": [
          11
      ],
      "targetIds": null,
      "fileSize": 5501737,
      "pageTotal": 42,
      "title": "军用电子元器件产业深度报告：信息化武器装备的精灵",
      "authors": "魏永,郭鑫",
      "orgName": "中航证券",
      "orgIds": [
          9306
      ],
      "publishAt": "2023-01-16T16:00:00.000Z",
      "uploaderName": "Ricki",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/e72be4a903348ca6a01ac6980a172bace55a560a.png",
      "stockName": null,
      "isHorizontal": true,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "<em>军用</em>电子元器件产业深度报告：信息化武器装备的精灵"
          ],
          "content": [
              "3.1.2<em>军用</em>数字芯片\n3.1.3<em>军用</em>传感器\n3.2<em>军用</em>被动元器件\n3.2.1<em>军用</em>RCL（容阻感）\n3.2.2<em>军用</em>连接器\n四、投资策略\n4.1投资逻辑\n4.2投资图谱\n目录\n\n一、产业特点——高壁垒、",
              "惯性测量\n以惯性技术为基础，融合卫星测量、摄影测量、红外测量、磁场测量等信息，通过多\n传感器融合技术，实现高精度的运动参数测量、姿态航向测量、运动轨迹测量等应用\n惯性稳控\n根据惯性组合输出的运动参数，通过<em>伺服</em>控制系统对任务平台的进行动态调整",
              "基于MEMS的光学识别与通信系统\n（MOIS）\n基于MEMS<em>伺服</em>系统的导弹“SAVAGE”\n基于各类MEMS传感器的单兵作战系统\nMEMS传感器工作原理\n\n三、发展现状——下游应用广泛，增长确定性高\n26",
              "受益于<em>军用</em>电子行业景气度提升，国产替代进程加速，我们认为主要投资方向包括：<em>军用</em>模拟芯片、<em>军用</em>数字芯片、<em>军用</em>传感器、<em>军用</em>RCL（容阻感）和<em>军用</em>连接器。",
              "<em>军用</em>数字芯片\n<em>军用</em>传感器\n<em>军用</em>RCL（容阻感）\n主\n要\n投\n资\n方\n向\n<em>军用</em>连接器\n\n四、投资策略\n37\n4.2投资图谱\n资料来源：中航证券研究所\n特\n种\n集\n成\n电\n路\n<em>军用</em>模拟芯片\n振华风光国博电子"
          ]
      },
      "score": 21.977928
  },
  {
      "id": 3313236,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1619221,
      "pageTotal": 28,
      "title": "振华风光（688439）：军用模拟深耕多年，研发积累彰显优质产品力",
      "authors": "郑震湘,佘凌星,余平",
      "orgName": "国盛证券",
      "orgIds": [
          9543
      ],
      "publishAt": "2022-09-15T01:29:17.000Z",
      "uploaderName": "悦欣凌羽",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/5058cd26dad797f6d0a5ef10379754b86bc94bae.png",
      "stockName": "振华风光",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "振华风光（688439）：<em>军用</em>模拟深耕多年，研发积累彰显优质产品力"
          ],
          "content": [
              "请仔细阅读本报告末页声明 \n证券研究报告 | 首次覆盖报告 \n2022年09月15日 \n振华风光（688439.SH） \n<em>军用</em>模拟深耕多年，研发积累彰显优质产品力 \n<em>军用</em>模拟IC老兵，业绩高速成长",
              "进口替代日趋旺盛，<em>军用</em>模拟空间可期。",
              "、弹载、\n车载、空间 \n1项已进入定型阶段；9项处于第三方鉴定阶段；10项正在\n进行样品测试和应用验证；3项正在流片加工；3项正在设\n计仿真中 \n系统封装集\n成电路 \n21 \n空间路由系统封装电路、\n<em>伺服</em>放大系统",
              "、数据采集\n系统 \n机载、弹载、\n车载、舰载 \n2项<em>伺服</em>系统项目已完成定型；5项进入第三方鉴定阶段；\n13项正在进行样品测试和应用验证；1项完成了系统总体方\n案设计 \n电源管理器 16 电压基准、电源管理",
              "转换器，其中放大器主要应用于武器装备中信号传输、电机驱动、仪器仪表、信号调理\n等场景，接口驱动主要应用于信号传输、数据交换等场景，系统封装集成电路主要应用\n于模拟前端、功率放大、各种传感器信号调理、<em>伺服</em>控制等场景"
          ]
      },
      "score": 21.298414
  },
  {
      "id": 3323431,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 3524260,
      "pageTotal": 28,
      "title": "振华风光（688439）公司深度研究：军用模拟IC领先企业，打造IDM模式发展",
      "authors": "杨晨",
      "orgName": "国金证券",
      "orgIds": [
          9551
      ],
      "publishAt": "2022-09-28T05:22:40.000Z",
      "uploaderName": "试着忘记",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/000c7ea67cc78f809e21bdeb6c234d95900a8d75.png",
      "stockName": "振华风光",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "振华风光（688439）公司深度研究：<em>军用</em>模拟IC领先企业，打造IDM模式发展"
          ],
          "content": [
              "<em>军用</em>装备对芯片自主安全需求突出，国\n产化率提升背景下，具备芯片自主可控能力的企业将获得更高市场份额。国\n内<em>军用</em>模拟厂商主要为传统军工企业，产品方向各有侧重，竞争格局稳定。",
              "投资建议 \n 公司为国内<em>军用</em>模拟IC领先企业，<em>军用</em>模拟IC赛道坡长雪厚，公司自研芯\n片产品储备充分、国产化替代下市场份额有望继续提升。",
              "预计未来5-10年，\n我国<em>军用</em>模拟芯片将实现完全自主可控，国产化需求显著提升，<em>军用</em>模拟\n芯片企业将迎来发展的黄金时期。",
              "级超低漏电流设计技术、±35KVESD的接口电路设计技术、高压大功\n率驱动器件布局布线技术、基于SOC的高压大功率驱动技术 \n机载、弹载、\n车载、舰载 \n系统封\n装集成\n电路 \n21 \n空间路由系统封装\n电路、<em>伺服</em>放大系",
              "统、数据采集系统 \n高阶<em>伺服</em>系统设计技术、硅基板多层布线技术、硅通孔技术 \n机载、弹载、\n车载、空间 \n电源管\n理器 \n16 \n电压基准、电源管\n理 \n全负载效率提升技术、精确过流保护技术、高阶温度补偿及多位修调设"
          ]
      },
      "score": 20.673264
  },
  {
      "id": 3456245,
      "typeId": 10,
      "businessId": 13,
      "labelIds": [
          11,
          31
      ],
      "targetIds": null,
      "fileSize": 1999389,
      "pageTotal": 42,
      "title": "军用模块电源：用电功率提升驱动需求高增长，头部企业扩产集中度有望提升",
      "authors": "鲍学博",
      "orgName": "中邮证券",
      "orgIds": [
          9316
      ],
      "publishAt": "2023-03-13T16:00:00.000Z",
      "uploaderName": "太阳西下了",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/5e39eb110d640880c9e6decfef1937bbbbb4cdf9.png",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "<em>军用</em>模块电源：用电功率提升驱动需求高增长，头部企业扩产集中度有望提升"
          ],
          "content": [
              "在国内<em>军用</em>装备数量补齐、新型装备列装、新\n型装备中价值量提升等多重因素驱动下，<em>军用</em>模块电源需求有望高增\n长。随着国家对装备“自主可控”要求的提升，全国产化产品需求强\n烈。",
              "模块电源具有更高的功率密度和更高的可靠性，<em>军用</em>优势显著。\n在国内<em>军用</em>装备数量补齐、新型装备列装、新型装备中价值量提升等\n多重因素驱动下，<em>军用</em>模块电源需求有望高增长。",
              "2.2 多因素驱动模块电源需求高增长，全国产化产品需求旺盛 \n在国内<em>军用</em>装备数量补齐、新型装备列装、新型装备中价值量提升等多重因\n素驱动下，<em>军用</em>模块电源需求有望高增长。",
              "在国内<em>军用</em>\n装备数量补齐、新型装备列装、新型装备中价值量提升等多重因素驱动下，<em>军用</em>\n\n \n请务必阅读正文之后的免责条款部分      29 \n模块电源需求有望高增长。",
              "具备完整电源变换器功\n能的器件，具有体积小、可靠性高、安装使用方便等特点，广泛应用于航空、航\n天、船舶、铁路、电力等对电源可靠性要求高的领域，例如：机载信号系统、驱\n动器控制器、隔离信号传输系统、CAN总线供电、<em>伺服</em>电机系统"
          ]
      },
      "score": 19.985468
  },
  {
      "id": 3419378,
      "typeId": 10,
      "businessId": 13,
      "labelIds": [
          11
      ],
      "targetIds": null,
      "fileSize": 7400776,
      "pageTotal": 74,
      "title": "军用无人机行业深度报告：作战新势下深度部署，万里长空上曙光初露",
      "authors": "王凯,刘宇辰",
      "orgName": "光大证券",
      "orgIds": [
          9391
      ],
      "publishAt": "2023-01-31T01:27:16.000Z",
      "uploaderName": "瓦莱丽",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/8e031b15b91f9143ae27f85a214304ab129d829c.png",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "<em>军用</em>无人机行业深度报告：作战新势下深度部署，万里长空上曙光初露"
          ],
          "content": [
              "带有双余度<em>伺服</em>操纵机构的V\n形全动尾翼不仅可以有效减少侧向雷达回波，还\n能屏蔽发动机尾喷流的红外特征。",
              "飞行器机体 附件舱、后设备舱底座、前舱航电底座、除冰控制器、结冰探测器 \n动力装置与能源 燃油蓄电池、发动机冷却风扇、滑油冷却器/散热器、发动机 \n飞行控制与导航 \nINS/GPS装置、GPS天线、尾翼<em>伺服</em>系统",
              "光电任务载荷要发挥功能大多需\n要安装在云台上以实现水平和竖直方向的转动，即光电吊舱=云台（电机<em>伺服</em>系\n统）+光电设备+软件。",
              "因我国<em>军用</em>无人机行业起步相对较晚但发展迅速，我们假设我国<em>军用</em>无人机列装\n需求规模滞后于美国一年，以美国2023年<em>军用</em>无人机费用占军费比例推算出我\n国2022年<em>军用</em>无人机装备需求规模约为192.9亿元（2022",
              "2011-2021年我国<em>军用</em>\n无人机出口数量最多的国家为巴基斯坦，共出口108架<em>军用</em>无人机，其次为沙\n特阿拉伯和埃及，分别出口70架、60架<em>军用</em>无人机。"
          ]
      },
      "score": 19.965841
  },
  {
      "id": 3346422,
      "typeId": 10,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 2170677,
      "pageTotal": 33,
      "title": "机械设备行业机器人系列深度报告：伺服电机，机器人关节动力源，看好国产厂商崛起",
      "authors": "",
      "orgName": "申万宏源",
      "orgIds": [
          9905
      ],
      "publishAt": "2022-10-25T16:00:00.000Z",
      "uploaderName": "霍华德",
      "indexImageUrl": "",
      "stockName": null,
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "机械设备行业机器人系列深度报告：<em>伺服</em>电机，机器人关节动力源，看好国产厂商崛起"
          ],
          "content": [
              "①<em>伺服</em>驱动器（指令装置）属于驱动层，\n又称“ <em>伺服</em> 控制 器” 、“ <em>伺服</em> 放大器 ”， 一般 通过 位置 、速 度和 力矩三 种方 式对 <em>伺服</em> 电机\n进行控 制， 实现 高精 度的 传动 系统定 位；",
              "高\n性能的<em>伺服</em>系统大多采用永磁同步交流<em>伺服</em>电动机，控制驱动器多采用快速、准确定位的\n全数字位置<em>伺服</em>系统。",
              "表3：直流<em>伺服</em>电机VS交流<em>伺服</em>电机 \n \n直流<em>伺服</em>电机 交流<em>伺服</em>电机 \n机械性能和调\n节性能 \n机械特性硬，线性度好，不同控制电压下斜率相同，堵\n转转矩大，调速范围广 \n机械特性软、非线性，不同控制电压下斜率不同",
              "1）需要 快速响 应的系\n统：<em>军用</em> 领域导 弹方向 的快速 调节、高灵敏 度的记 录和检 测设备、工业机 器人、仿生义 肢；\n2）对重 量和能 耗要 求的飞 行器 ，包括 无人 机、航 模等 ；3）其",
              "公司掌 握高\n性能<em>伺服</em> 控制技 术、高性 能<em>伺服</em> 电机技 术等核 心技 术，产品 矩阵丰 富，覆盖单轴/多轴 <em>伺服</em>\n系统、通 用/专用伺 服系统、 新一代 <em>伺服</em>系 统、电 液<em>伺服</em> 系统、高 精度 <em>伺服</em>驱"
          ]
      },
      "score": 19.580704
  },
  {
      "id": 3509302,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1329801,
      "pageTotal": 5,
      "title": "伟创电气（688698）：伺服盈利提升显著，海外业务驶入快车道",
      "authors": "韩晨,李昂",
      "orgName": "西南证券",
      "orgIds": [
          10071
      ],
      "publishAt": "2023-04-18T11:13:48.000Z",
      "uploaderName": "司徒文翰",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/3b466e505227c3ebf8d9df9390287c7ded8b2a81.png",
      "stockName": "伟创电气",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "伟创电气（688698）：<em>伺服</em>盈利提升显著，海外业务驶入快车道"
          ],
          "content": [
              "Table_StockInfo] \n2023年04月17日 \n证 券研究报告•2022年 年报点评 \n持有 \n（ 维持） \n \n当前价： 26.76元 \n伟创电气（688698） \n电 力设备 \n目标价： ——元（6个月） \n<em>伺服</em>盈利提升显著",
              "伟创电气（688698）：经营状况良好，\n<em>伺服</em>及控制系统表现两眼 (2022-04-18) \n  \n[Table_Summary] \n 事件：2022年，公司实现营收9.1亿元，同比增长10.6%；实现归母净利润",
              "<em>伺服</em>系统发展的核心在于降本+产品迭代，公司目前在研项目\n中，①磁电编码器：位于开发验证阶段，24年有望实现批量出货，公司将在已\n实现光编自研基础上，进一步降低<em>伺服</em>电机成本。",
              "假设3：<em>伺服</em>及运动控制器产能高速增长，产能利用率有望逐步提升。预计2023-2025\n年公司<em>伺服</em>系统及运动控制器销量增速分别约为24%/40%/30%。",
              "假设4：<em>伺服</em>系统行业竞争激烈，未来可能存在价格战，假设公司<em>伺服</em>产品单价年降。"
          ]
      },
      "score": 19.551384
  },
  {
      "id": 3031796,
      "typeId": 16,
      "businessId": 4,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 376863,
      "pageTotal": 6,
      "title": "北交所策略事件点评：星辰科技：核心产品军用伺服稳增，工业控制领域受益下游高景气",
      "authors": "诸海滨,赵昊",
      "orgName": "安信证券",
      "orgIds": [
          9601
      ],
      "publishAt": "2022-04-05T16:00:00.000Z",
      "uploaderName": "Acker",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/306762fed81b9ba9453687a6acb09698f60a02b8.png",
      "stockName": "星辰科技",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "北交所策略事件点评：星辰科技：核心产品<em>军用</em><em>伺服</em>稳增，工业控制领域受益下游高景气"
          ],
          "content": [
              "■2021年公司军工类收入8479万元，占总收入比重60%，毛利率持续提升至71%：\n在“自主可控”政策的持续推进下，公司作为军工<em>伺服</em>系统国产化领军人，较早\n投入<em>军用</em>产品100%国产化工作。",
              "2021年4月公司获批承担2021年广西科技重大\n专项项目“<em>军用</em>系列<em>伺服</em>驱动器百分之百国产化研制及产业化”，为公司发展注\n入新动力。",
              "公司在<em>军用</em>装备制造领域的配套层级\n逐步从<em>伺服</em>驱动器、双电机消隙系统、<em>伺服</em>电机等“部件级”配套向<em>军用</em>调平系\n统、天线回转和倒伏机构、<em>军用</em>无人车驱控系统等“总成级”配套发展，使得公\n司在<em>军用</em>装备配套领域重要性日益提升",
              "■投资建议：公司专注<em>伺服</em>系统，在军工领域深耕多年，在国内<em>军用</em><em>伺服</em>行业占\n据优势地位。目前公司正逐步完善发展布局，向新能源、工业控制领域深入发展。",
              "公司拟募资1.68亿元，主要用于<em>军用</em>随动控制总成产业化及<em>伺服</em>电机扩产项目和\n研发中心建设，同时拟发行170万股开展股权激励计划，为公司可持续发展提供\n支持。"
          ]
      },
      "score": 19.385635
  },
  {
      "id": 3388488,
      "typeId": 16,
      "businessId": 13,
      "labelIds": [
          11
      ],
      "targetIds": null,
      "fileSize": 3306248,
      "pageTotal": 35,
      "title": "激光振镜控制系统隐形冠军，进军硬件和伺服控制领域",
      "authors": "刘卓",
      "orgName": "中邮证券",
      "orgIds": [
          9316
      ],
      "publishAt": "2022-12-12T16:00:00.000Z",
      "uploaderName": "Viola",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/636db87fb86c11817d2f123006bb91b44cc37956.png",
      "stockName": "金橙子",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "激光振镜控制系统隐形冠军，进军硬件和<em>伺服</em>控制领域"
          ],
          "content": [
              "此外，公司发挥技术和渠道协同优势，横向拓展激光<em>伺服</em>控制业\n务。",
              "我们测算国内激光<em>伺服</em>控制系统市场规模超20亿，其中高端市\n场约19亿，主要受外资主导，我们预计到2025年国内激光<em>伺服</em>控制\n系统高端市场空间有望达到30亿左右。",
              "振镜控制聚焦于“高精密+超快+小幅面”，<em>伺服</em>控制焦距于“高功率”。振镜控制与\n<em>伺服</em>控制系统分别在不同应用场景各具优势。",
              "我们认为金橙子将凭借在激光设备振镜领域积累的技术优势和客户群体，逐步切入<em>伺服</em>控制\n系统，预计激光加工<em>伺服</em>系统也将是公司未来一个重要发力点，公司将逐步拓展<em>伺服</em>系统业务，\n我们预计2022E-2024E公司在激光加工<em>伺服</em>系统方面的市场占有率为",
              "3、<em>伺服</em>控制系统市场拓展不达预期风险 \n公司在对既有振镜控制产品进行升级迭代的基础上，亦布局并推出激光<em>伺服</em>控制系统，主\n要应用于激光切割领域。"
          ]
      },
      "score": 18.756893
  },
  {
      "id": 3306095,
      "typeId": 16,
      "businessId": 4,
      "labelIds": [
          25
      ],
      "targetIds": null,
      "fileSize": 3030301,
      "pageTotal": 37,
      "title": "军用电子元器件大本营，平台化发展前景光明",
      "authors": "陈睿彬",
      "orgName": "东吴证券国际",
      "orgIds": [
          9130
      ],
      "publishAt": "2022-09-01T16:00:00.000Z",
      "uploaderName": "凯尔特",
      "indexImageUrl": "",
      "stockName": "振华科技",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "<em>军用</em>电子元器件大本营，平台化发展前景光明"
          ],
          "content": [
              "2000-2007\n<em>军用</em>国外元器\n件需要进口\n鸿远电子成立\n自产、代理业务并\n行\n成熟期2007至今\n民用市场：国\n外元器件处于\n领先地位\n新玩家逐步进\n入<em>军用</em>电子元\n器件领域\n<em>军用</em>电子元\n器件国产替",
              "<em>军用</em>电子元器件大本营，平台化发展前景光明 \n2.1.   振华新云—国内<em>军用</em>钽电容领域核心供应商 \n2.1.1.",
              "振华云科—国内<em>军用</em>片式电阻器龙头企业 \n振华云科是国内片式厚膜固定电阻器中品种最多、规格最齐全的军品生产厂家，占\n有国内<em>军用</em>电阻器85%以上的市场份额，是国内<em>军用</em>片式电阻器龙头。",
              "森未科技研发产品包括\nIGBT芯片及封装器件2大类，电压等级覆盖600V-1700V，单芯片电流规格覆盖2A-\n200A，单管和模块产品电流规格覆盖2A-800A，覆盖工业控制、变频家电、电动汽车、\n风电<em>伺服</em>驱动",
              "过去我国<em>军用</em>IGBT绝大\n部分依靠进口，目前逐步开始国产替代；新型武器装备电气电动化趋势明显，未来5-10\n年<em>军用</em>IGBT行业将持续高增长。"
          ]
      },
      "score": 18.065828
  },
  {
      "id": 3389102,
      "typeId": 16,
      "businessId": 9,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 1296225,
      "pageTotal": 25,
      "title": "智能化无人装备领域的潜力新星",
      "authors": "郑小霞,邓承佯",
      "orgName": "华安证券",
      "orgIds": [
          9465
      ],
      "publishAt": "2022-12-13T16:00:00.000Z",
      "uploaderName": "苹果苹果",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/51e1b5f284aea201ac95139099d443f4e0bdca5e.png",
      "stockName": "晶品特装",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "content": [
              "按照客户实际作战需求，不同产品按需求可集成不同功能模块\n以形成更为复杂的功能，包括卫星定位、电子罗盘、惯性测量、<em>伺服</em>控制、激光测\n距、存储、信息显示等。",
              "证券研究报告 \n图表13 光电侦察设备业务主要产品种类及应用 \n产品类型 产品系列 产品简介 应用领域 \n无\n人\n机\n光\n电\n吊\n舱 \n小型固定\n翼无人机\n吊舱 \n \n具有高清白光/红外昼夜侦察、双轴<em>伺服</em>稳",
              "<em>军用</em>、民用小型\n固定翼无人机。 \n小型旋翼\n无人机吊\n舱 \n \n集成高清白光、红外成像、激光照明等传\n感器，结合稳定<em>伺服</em>平台，具有昼夜侦察、\n目标稳定跟踪等功能。 \n<em>军用</em>、民用小型 \n旋翼无人机。",
              "光电探测\n系统、吊\n舱<em>伺服</em>控\n制系统、\n耐辐射相\n机、强光\n拒止器等 \n \n结合现有核心技术及产品，可向各类军民\n客户提供光电探测系统、<em>伺服</em>控制系统、\n耐辐射相机等系统/组件光电相关产品。",
              "购分类 \n需求对应的产品类型 \n光电成像 \n光学系统可见光探测\n器红外探测器微光组\n件 \n设计、定制化采购、\n检测、组装 \n光电组件电子\n器件 \n无人机光电吊舱、手持光电\n侦察设备、单兵夜视镜 \n稳定<em>伺服</em>"
          ]
      },
      "score": 17.933933
  },
  {
      "id": 3400484,
      "typeId": 16,
      "businessId": 4,
      "labelIds": [],
      "targetIds": null,
      "fileSize": 2891312,
      "pageTotal": 29,
      "title": "禾川科技（688320）：国产伺服系统引领者，产业链上下游联动助力",
      "authors": "李鲁靖,朱晔",
      "orgName": "天风证券",
      "orgIds": [
          9584
      ],
      "publishAt": "2022-12-30T05:41:04.000Z",
      "uploaderName": "北辰°浅巷墨漓",
      "indexImageUrl": "https://storage.djyanbao.com/dj-docs/503f2d1d09c8e1ea77db474ca8f016e8b9a2825e.png",
      "stockName": "禾川科技",
      "isHorizontal": false,
      "canConvert": true,
      "hasDownloaded": false,
      "highlight": {
          "title": [
              "禾川科技（688320）：国产<em>伺服</em>系统引领者，产业链上下游联动助力"
          ],
          "content": [
              "其中，<em>伺服</em>系统类包括交\n流<em>伺服</em>驱动器、交流<em>伺服</em>电机、低压<em>伺服</em>驱动器、低压<em>伺服</em>电机、一体式<em>伺服</em>电机等；控制\n技术类包括可编程运动控制器、运动控制卡、远程 IO 模块、人机界面、机器视觉等。",
              "<em>伺服</em>系统可分为通用<em>伺服</em>系统和专用<em>伺服</em>系统。",
              "截止2021年以来，国务院、国家发改委、工业和信息化部等多部门都陆续印发了支持、\n规范<em>伺服</em>电机行业的发展政策，内容涉及<em>伺服</em>电机发展营商环境、<em>伺服</em>电机技术发展路线、\n<em>伺服</em>电机规范和标准等内容。",
              "<em>伺服</em>驱动器：公司在<em>伺服</em>驱动器领域拥有<em>伺服</em>系统三环综合矢量控制技术、新型<em>伺服</em>控\n制技术、高级智能调整算法技术、高速总线控制技术等核心技术。",
              "若未来<em>伺服</em>\n系统市场的竞争进一步加剧、出现完全替代<em>伺服</em>系统的新产品、或公司的<em>伺服</em>系统无法\n适应行业发展和客户需求，则将导致公司的<em>伺服</em>系统产品收入下滑，并对公司的经营与\n发展产生不利影响。"
          ]
      },
      "score": 17.704473
  }
]

const json = data.filter(i => i.pageTotal > 10).map((i,index) => ({
  '序号': index+1,
  '摘要': i.highlight.content,
  '时间': i.publishAt?.slice(0,10),
  '页数': i.pageTotal
}))

const jsonData = JSON.stringify(json, null, 2);

// fs.writeFile('data.json', jsonData, (err) => {
//   if (err) throw err;
//   console.log('Data written to file');
// });

const server = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Access-Control-Allow-Origin', 'http://localhost:52330');
  res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE');
  res.setHeader('Access-Control-Allow-Headers', 'Content-Type');
  res.setHeader('Content-Type', 'application/json; charset=utf-8');
  res.end(jsonData);
});

server.listen(port, () => {
  console.log(`Server running at http://localhost:${port}/`);
});