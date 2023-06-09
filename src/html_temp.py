# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup


def extract_span_contents(html):
    soup = BeautifulSoup(html, 'html.parser')
    span_contents = []
    for span in soup.find_all('span'):
        span_contents.append(span.get_text())
    return span_contents


print(123)
html = '''
<html><head>
    <title>授信订单详情</title>
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta http-equiv="content-type" content="text/html; charset=utf-8">
    <link href="resources/css/axure_rp_page.css" type="text/css" rel="stylesheet">
    <link href="data/styles.css" type="text/css" rel="stylesheet">
    <link href="files/授信订单详情/styles.css" type="text/css" rel="stylesheet">
    <script src="resources/scripts/jquery-3.2.1.min.js"></script>
    <script src="resources/scripts/axure/axQuery.js"></script>
    <script src="resources/scripts/axure/globals.js"></script>
    <script src="resources/scripts/axutils.js"></script>
    <script src="resources/scripts/axure/annotation.js"></script>
    <script src="resources/scripts/axure/axQuery.std.js"></script>
    <script src="resources/scripts/axure/doc.js"></script>
    <script src="resources/scripts/messagecenter.js"></script>
    <script src="resources/scripts/axure/events.js"></script>
    <script src="resources/scripts/axure/recording.js"></script>
    <script src="resources/scripts/axure/action.js"></script>
    <script src="resources/scripts/axure/expr.js"></script>
    <script src="resources/scripts/axure/geometry.js"></script>
    <script src="resources/scripts/axure/flyout.js"></script>
    <script src="resources/scripts/axure/model.js"></script>
    <script src="resources/scripts/axure/repeater.js"></script>
    <script src="resources/scripts/axure/sto.js"></script>
    <script src="resources/scripts/axure/utils.temp.js"></script>
    <script src="resources/scripts/axure/variables.js"></script>
    <script src="resources/scripts/axure/drag.js"></script>
    <script src="resources/scripts/axure/move.js"></script>
    <script src="resources/scripts/axure/visibility.js"></script>
    <script src="resources/scripts/axure/style.js"></script>
    <script src="resources/scripts/axure/adaptive.js"></script>
    <script src="resources/scripts/axure/tree.js"></script>
    <script src="resources/scripts/axure/init.temp.js"></script>
    <script src="resources/scripts/axure/legacy.js"></script>
    <script src="resources/scripts/axure/viewer.js"></script>
    <script src="resources/scripts/axure/math.js"></script>
    <script src="resources/scripts/axure/jquery.nicescroll.min.js"></script>
    <script src="data/document.js"></script>
    <script src="files/授信订单详情/data.js"></script>
    <script type="text/javascript">
      $axure.utils.getTransparentGifPath = function() { return 'resources/images/transparent.gif'; };
      $axure.utils.getOtherPath = function() { return 'resources/Other.html'; };
      $axure.utils.getReloadPath = function() { return 'resources/reload.html'; };
    </script>
  </head>
  <body>
    <div id="base" class="">

      <!-- Unnamed (Rectangle) -->
      <div id="u0" class="ax_default box_2">
        <div id="u0_div" class=""></div>
        <div id="u0_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1" class="ax_default box_1">
        <div id="u1_div" class=""></div>
        <div id="u1_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u2" class="ax_default box_1">
        <div id="u2_div" class=""></div>
        <div id="u2_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u3" class="ax_default box_1">
        <div id="u3_div" class=""></div>
        <div id="u3_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u4" class="ax_default" data-left="946" data-top="119" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u5" class="ax_default _图片_">
          <img id="u5_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u5_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u6" class="ax_default box_1">
          <div id="u6_div" class=""></div>
          <div id="u6_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u7" class="ax_default _图片_">
          <img id="u7_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u7_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u8" class="ax_default box_1">
          <div id="u8_div" class=""></div>
          <div id="u8_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u9" class="ax_default _图片_">
          <img id="u9_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u9_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u10" class="ax_default box_1">
          <div id="u10_div" class=""></div>
          <div id="u10_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u12" class="ax_default box_1">
        <div id="u12_div" class=""></div>
        <div id="u12_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u13" class="ax_default box_1">
        <div id="u13_div" class=""></div>
        <div id="u13_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u14" class="ax_default" data-left="0" data-top="164" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u15" class="ax_default box_1">
          <div id="u15_div" class=""></div>
          <div id="u15_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u16" class="ax_default _图片_">
          <img id="u16_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u16_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u17" class="ax_default box_1">
          <div id="u17_div" class=""></div>
          <div id="u17_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u18" class="ax_default box_1">
          <div id="u18_div" class=""></div>
          <div id="u18_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u19" class="ax_default box_1">
        <div id="u19_div" class=""></div>
        <div id="u19_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u20" class="ax_default box_1">
        <div id="u20_div" class=""></div>
        <div id="u20_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u21" class="ax_default box_1">
        <img id="u21_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u21_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u22" class="ax_default box_1">
        <div id="u22_div" class=""></div>
        <div id="u22_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u23" class="ax_default box_1">
        <div id="u23_div" class=""></div>
        <div id="u23_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u24" class="ax_default box_1">
        <div id="u24_div" class=""></div>
        <div id="u24_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u25" class="ax_default box_1">
        <div id="u25_div" class=""></div>
        <div id="u25_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u26" class="ax_default box_1">
        <div id="u26_div" class=""></div>
        <div id="u26_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u27" class="ax_default box_1">
        <div id="u27_div" class=""></div>
        <div id="u27_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u11" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u28" class="ax_default" data-left="214" data-top="179" data-width="141" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u29" class="ax_default _文本">
          <div id="u29_div" class="" tabindex="0"></div>
          <div id="u29_text" class="text ">
            <p><span>授信订单详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u30" class="ax_default icon">
          <img id="u30_img" class="img " src="images/授信订单详情/regen/u30.svg">
          <div id="u30_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u31" class="ax_default" data-left="252" data-top="673" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u32" class="ax_default line">
          <img id="u32_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u32_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u33" class="ax_default box_2">
          <div id="u33_div" class=""></div>
          <div id="u33_text" class="text ">
            <p><span>授信主体信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u34" class="ax_default" data-left="289" data-top="337" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u35" class="ax_default _文本">
          <div id="u35_div" class=""></div>
          <div id="u35_text" class="text ">
            <p><span>授信申请编号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u36" class="ax_default _文本">
          <div id="u36_div" class=""></div>
          <div id="u36_text" class="text ">
            <p><span>DL20221010000001</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u37" class="ax_default" data-left="834" data-top="372" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u38" class="ax_default _文本">
          <div id="u38_div" class=""></div>
          <div id="u38_text" class="text ">
            <p><span>产品名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u39" class="ax_default _文本">
          <div id="u39_div" class=""></div>
          <div id="u39_text" class="text ">
            <p><span>XXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u40" class="ax_default" data-left="252" data-top="442" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u41" class="ax_default _文本">
          <div id="u41_div" class=""></div>
          <div id="u41_text" class="text ">
            <p><span>申请金额(元)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u42" class="ax_default _文本">
          <div id="u42_div" class=""></div>
          <div id="u42_text" class="text ">
            <p><span>100,000.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u43" class="ax_default" data-left="834" data-top="442" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u44" class="ax_default _文本">
          <div id="u44_div" class=""></div>
          <div id="u44_text" class="text ">
            <p><span>申请期限(月)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u45" class="ax_default _文本">
          <div id="u45_div" class=""></div>
          <div id="u45_text" class="text ">
            <p><span>3</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u46" class="ax_default" data-left="841" data-top="477" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u47" class="ax_default _文本">
          <div id="u47_div" class=""></div>
          <div id="u47_text" class="text ">
            <p><span>还款方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u48" class="ax_default _文本">
          <div id="u48_div" class=""></div>
          <div id="u48_text" class="text ">
            <p><span>等额本息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u49" class="ax_default" data-left="289" data-top="477" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u50" class="ax_default _文本">
          <div id="u50_div" class=""></div>
          <div id="u50_text" class="text ">
            <p><span>贷款用途</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u51" class="ax_default _文本">
          <div id="u51_div" class=""></div>
          <div id="u51_text" class="text ">
            <p><span>日常经营</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u52" class="ax_default" data-left="815" data-top="512" data-width="328" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u53" class="ax_default _文本">
          <div id="u53_div" class=""></div>
          <div id="u53_text" class="text ">
            <p><span>客户经理</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u54" class="ax_default _文本">
          <div id="u54_div" class=""></div>
          <div id="u54_text" class="text ">
            <p><span>吴帆</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u55" class="ax_default" data-left="292" data-top="407" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u56" class="ax_default _文本">
          <div id="u56_div" class=""></div>
          <div id="u56_text" class="text ">
            <p><span>担保方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u57" class="ax_default _文本">
          <div id="u57_div" class=""></div>
          <div id="u57_text" class="text ">
            <p><span>抵押</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u58" class="ax_default" data-left="841" data-top="547" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u59" class="ax_default _文本">
          <div id="u59_div" class=""></div>
          <div id="u59_text" class="text ">
            <p><span>申请时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u60" class="ax_default _文本">
          <div id="u60_div" class=""></div>
          <div id="u60_text" class="text ">
            <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">2020-09-01 hh</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">mm</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">ss</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u61" class="ax_default" data-left="292" data-top="547" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u62" class="ax_default _文本">
          <div id="u62_div" class=""></div>
          <div id="u62_text" class="text ">
            <p><span>授信状态</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u63" class="ax_default _文本">
          <div id="u63_div" class=""></div>
          <div id="u63_text" class="text ">
            <p><span>预授信拒绝</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u64" class="ax_default" data-left="252" data-top="995" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u65" class="ax_default line">
          <img id="u65_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u65_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u66" class="ax_default box_2">
          <div id="u66_div" class=""></div>
          <div id="u66_text" class="text ">
            <p><span>关联企业信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u67" class="ax_default" data-left="292" data-top="372" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u68" class="ax_default _文本">
          <div id="u68_div" class=""></div>
          <div id="u68_text" class="text ">
            <p><span>渠道来源</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u69" class="ax_default _文本">
          <div id="u69_div" class=""></div>
          <div id="u69_text" class="text ">
            <p><span>XX渠道</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u70" class="ax_default" data-left="810" data-top="731" data-width="362" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u71" class="ax_default _文本">
          <div id="u71_div" class=""></div>
          <div id="u71_text" class="text ">
            <p><span>证件号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u72" class="ax_default _文本">
          <div id="u72_div" class=""></div>
          <div id="u72_text" class="text ">
            <p><span>110102197901021234</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u73" class="ax_default" data-left="292" data-top="731" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u74" class="ax_default _文本">
          <div id="u74_div" class=""></div>
          <div id="u74_text" class="text ">
            <p><span>客户名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u75" class="ax_default _文本">
          <div id="u75_div" class=""></div>
          <div id="u75_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u76" class="ax_default" data-left="834" data-top="337" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u77" class="ax_default _文本">
          <div id="u77_div" class=""></div>
          <div id="u77_text" class="text ">
            <p><span>网贷申请编号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u78" class="ax_default _文本">
          <div id="u78_div" class=""></div>
          <div id="u78_text" class="text ">
            <p><span>DL20221010000001</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u79" class="ax_default" data-left="834" data-top="407" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u80" class="ax_default _文本">
          <div id="u80_div" class=""></div>
          <div id="u80_text" class="text ">
            <p><span>授信主体</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u81" class="ax_default _文本">
          <div id="u81_div" class=""></div>
          <div id="u81_text" class="text ">
            <p><span>个人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u82" class="ax_default" data-left="263" data-top="512" data-width="328" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u83" class="ax_default _文本">
          <div id="u83_div" class=""></div>
          <div id="u83_text" class="text ">
            <p><span>申请机构</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u84" class="ax_default _文本">
          <div id="u84_div" class=""></div>
          <div id="u84_text" class="text ">
            <p><span>10,000.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u85" class="ax_default" data-left="289" data-top="1708" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u86" class="ax_default _文本">
          <div id="u86_div" class=""></div>
          <div id="u86_text" class="text ">
            <p><span>额度状态</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u87" class="ax_default _文本">
          <div id="u87_div" class=""></div>
          <div id="u87_text" class="text ">
            <p><span>-</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u88" class="ax_default" data-left="292" data-top="764" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u89" class="ax_default _文本">
          <div id="u89_div" class=""></div>
          <div id="u89_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u90" class="ax_default _文本">
          <div id="u90_div" class=""></div>
          <div id="u90_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u91" class="ax_default" data-left="252" data-top="1510" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u92" class="ax_default line">
          <img id="u92_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u92_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u93" class="ax_default box_2">
          <div id="u93_div" class=""></div>
          <div id="u93_text" class="text ">
            <p><span>额度信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u94" class="ax_default" data-left="252" data-top="1577" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u95" class="ax_default _文本">
          <div id="u95_div" class=""></div>
          <div id="u95_text" class="text ">
            <p><span>授信额度(元)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u96" class="ax_default _文本">
          <div id="u96_div" class=""></div>
          <div id="u96_text" class="text ">
            <p><span>100,000.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u97" class="ax_default" data-left="289" data-top="1646" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u98" class="ax_default _文本">
          <div id="u98_div" class=""></div>
          <div id="u98_text" class="text ">
            <p><span>授信期限(月)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u99" class="ax_default _文本">
          <div id="u99_div" class=""></div>
          <div id="u99_text" class="text ">
            <p><span>3</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u100" class="ax_default" data-left="841" data-top="1646" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u101" class="ax_default _文本">
          <div id="u101_div" class=""></div>
          <div id="u101_text" class="text ">
            <p><span>还款方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u102" class="ax_default _文本">
          <div id="u102_div" class=""></div>
          <div id="u102_text" class="text ">
            <p><span>等额本息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u103" class="ax_default" data-left="246" data-top="1613" data-width="351" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u104" class="ax_default _文本">
          <div id="u104_div" class=""></div>
          <div id="u104_text" class="text ">
            <p><span>1年期授信利率(%)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u105" class="ax_default _文本">
          <div id="u105_div" class=""></div>
          <div id="u105_text" class="text ">
            <p><span>12</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u106" class="ax_default" data-left="226" data-top="1676" data-width="365" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u107" class="ax_default _文本">
          <div id="u107_div" class=""></div>
          <div id="u107_text" class="text ">
            <p><span>额度生效时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u108" class="ax_default _文本">
          <div id="u108_div" class=""></div>
          <div id="u108_text" class="text ">
            <p><span>2022-01-02</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u109" class="ax_default" data-left="841" data-top="764" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u110" class="ax_default _文本">
          <div id="u110_div" class=""></div>
          <div id="u110_text" class="text ">
            <p><span>性别</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u111" class="ax_default _文本">
          <div id="u111_div" class=""></div>
          <div id="u111_text" class="text ">
            <p><span>男</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u112" class="ax_default" data-left="292" data-top="796" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u113" class="ax_default _文本">
          <div id="u113_div" class=""></div>
          <div id="u113_text" class="text ">
            <p><span>民族</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u114" class="ax_default _文本">
          <div id="u114_div" class=""></div>
          <div id="u114_text" class="text ">
            <p><span>汉</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u115" class="ax_default" data-left="841" data-top="796" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u116" class="ax_default _文本">
          <div id="u116_div" class=""></div>
          <div id="u116_text" class="text ">
            <p><span>出生日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u117" class="ax_default _文本">
          <div id="u117_div" class=""></div>
          <div id="u117_text" class="text ">
            <p><span>2020-09-01</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u118" class="ax_default" data-left="292" data-top="824" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u119" class="ax_default _文本">
          <div id="u119_div" class=""></div>
          <div id="u119_text" class="text ">
            <p><span>住址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u120" class="ax_default _文本">
          <div id="u120_div" class=""></div>
          <div id="u120_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u121" class="ax_default" data-left="841" data-top="824" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u122" class="ax_default _文本">
          <div id="u122_div" class=""></div>
          <div id="u122_text" class="text ">
            <p><span>签发机关</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u123" class="ax_default _文本">
          <div id="u123_div" class=""></div>
          <div id="u123_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u124" class="ax_default" data-label="添加" title="未选择任何文件" data-left="406" data-top="892" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u125" class="ax_default box_1">
          <img id="u125_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u125_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u126" class="ax_default label">
        <div id="u126_div" class=""></div>
        <div id="u126_text" class="text ">
          <p><span>身份证人像面</span></p>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u127" class="ax_default" data-label="添加" title="未选择任何文件" data-left="951" data-top="897" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u128" class="ax_default box_1">
          <img id="u128_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u128_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u129" class="ax_default label">
        <div id="u129_div" class=""></div>
        <div id="u129_text" class="text ">
          <p><span>身份证国徽面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u130" class="ax_default" data-left="252" data-top="856" data-width="314" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u131" class="ax_default box_1">
          <div id="u131_div" class=""></div>
          <div id="u131_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u132" class="ax_default box_1">
          <div id="u132_div" class=""></div>
          <div id="u132_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u133" class="ax_default" data-left="807" data-top="849" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u134" class="ax_default box_1">
          <div id="u134_div" class=""></div>
          <div id="u134_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u135" class="ax_default box_1">
          <div id="u135_div" class=""></div>
          <div id="u135_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u136" class="ax_default" data-left="214" data-top="233" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u137" class="ax_default box_21">
          <div id="u137_div" class=""></div>
          <div id="u137_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u138" class="ax_default" data-left="263" data-top="233" data-width="712" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u139" class="ax_default box_21">
            <div id="u139_div" class=""></div>
            <div id="u139_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u140" class="ax_default box_21">
            <div id="u140_div" class=""></div>
            <div id="u140_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u141" class="ax_default box_21">
            <div id="u141_div" class=""></div>
            <div id="u141_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u142" class="ax_default box_21">
            <div id="u142_div" class=""></div>
            <div id="u142_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u143" class="ax_default box_21">
            <div id="u143_div" class=""></div>
            <div id="u143_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u144" class="ax_default" data-left="240" data-top="1764" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u145" class="ax_default line">
          <img id="u145_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u145_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u146" class="ax_default box_2">
          <div id="u146_div" class=""></div>
          <div id="u146_text" class="text ">
            <p><span>进度详情</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u147" class="ax_default" data-left="292" data-top="582" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u148" class="ax_default _文本">
          <div id="u148_div" class=""></div>
          <div id="u148_text" class="text ">
            <p><span>业务模式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u149" class="ax_default _文本">
          <div id="u149_div" class=""></div>
          <div id="u149_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u150" class="ax_default" data-left="841" data-top="582" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u151" class="ax_default _文本">
          <div id="u151_div" class=""></div>
          <div id="u151_text" class="text ">
            <p><span>所属商户</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u152" class="ax_default _文本">
          <div id="u152_div" class=""></div>
          <div id="u152_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u153" class="ax_default" data-left="211" data-top="612" data-width="383" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u154" class="ax_default _文本">
          <div id="u154_div" class=""></div>
          <div id="u154_text" class="text ">
            <p><span>是否指定担保公司</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u155" class="ax_default _文本">
          <div id="u155_div" class=""></div>
          <div id="u155_text" class="text ">
            <p><span>是</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u156" class="ax_default" data-left="760" data-top="612" data-width="383" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u157" class="ax_default _文本">
          <div id="u157_div" class=""></div>
          <div id="u157_text" class="text ">
            <p><span>担保公司</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u158" class="ax_default _文本">
          <div id="u158_div" class=""></div>
          <div id="u158_text" class="text ">
            <p><span>xx公司</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u159" class="ax_default" data-left="311" data-top="1427" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u160" class="ax_default box_1">
          <div id="u160_div" class=""></div>
          <div id="u160_text" class="text ">
            <p><span>支付方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u161" class="ax_default box_1">
          <div id="u161_div" class=""></div>
          <div id="u161_text" class="text ">
            <p><span>自主支付</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u162" class="ax_default" data-left="818" data-top="1456" data-width="366" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u163" class="ax_default box_1">
          <div id="u163_div" class=""></div>
          <div id="u163_text" class="text ">
            <p><span>账号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u164" class="ax_default box_1">
          <div id="u164_div" class=""></div>
          <div id="u164_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u165" class="ax_default" data-left="290" data-top="1452" data-width="319" data-height="32">

        <!-- Unnamed (Rectangle) -->
        <div id="u166" class="ax_default box_1">
          <div id="u166_div" class=""></div>
          <div id="u166_text" class="text ">
            <p><span>账号名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u167" class="ax_default box_1">
          <div id="u167_div" class=""></div>
          <div id="u167_text" class="text ">
            <p><span>XXXXXXX企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u168" class="ax_default" data-left="818" data-top="1427" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u169" class="ax_default box_1">
          <div id="u169_div" class=""></div>
          <div id="u169_text" class="text ">
            <p><span>借款用途</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u170" class="ax_default box_1">
          <div id="u170_div" class=""></div>
          <div id="u170_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u171" class="ax_default" data-left="252" data-top="1367" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u172" class="ax_default line">
          <img id="u172_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u172_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u173" class="ax_default box_2">
          <div id="u173_div" class=""></div>
          <div id="u173_text" class="text ">
            <p><span>支付信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u174" class="ax_default box_2">
        <div id="u174_div" class=""></div>
        <div id="u174_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u175" class="ax_default box_1">
        <div id="u175_div" class=""></div>
        <div id="u175_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u176" class="ax_default box_1">
        <div id="u176_div" class=""></div>
        <div id="u176_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u177" class="ax_default box_1">
        <div id="u177_div" class=""></div>
        <div id="u177_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u178" class="ax_default" data-left="2397" data-top="2401" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u179" class="ax_default _图片_">
          <img id="u179_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u179_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u180" class="ax_default box_1">
          <div id="u180_div" class=""></div>
          <div id="u180_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u181" class="ax_default _图片_">
          <img id="u181_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u181_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u182" class="ax_default box_1">
          <div id="u182_div" class=""></div>
          <div id="u182_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u183" class="ax_default _图片_">
          <img id="u183_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u183_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u184" class="ax_default box_1">
          <div id="u184_div" class=""></div>
          <div id="u184_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u186" class="ax_default box_1">
        <div id="u186_div" class=""></div>
        <div id="u186_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u187" class="ax_default box_1">
        <div id="u187_div" class=""></div>
        <div id="u187_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u188" class="ax_default" data-left="1451" data-top="2446" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u189" class="ax_default box_1">
          <div id="u189_div" class=""></div>
          <div id="u189_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u190" class="ax_default _图片_">
          <img id="u190_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u190_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u191" class="ax_default box_1">
          <div id="u191_div" class=""></div>
          <div id="u191_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u192" class="ax_default box_1">
          <div id="u192_div" class=""></div>
          <div id="u192_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u193" class="ax_default box_1">
        <div id="u193_div" class=""></div>
        <div id="u193_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u194" class="ax_default box_1">
        <div id="u194_div" class=""></div>
        <div id="u194_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u195" class="ax_default box_1">
        <img id="u195_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u195_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u196" class="ax_default box_1">
        <div id="u196_div" class=""></div>
        <div id="u196_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u197" class="ax_default box_1">
        <div id="u197_div" class=""></div>
        <div id="u197_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u198" class="ax_default box_1">
        <div id="u198_div" class=""></div>
        <div id="u198_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u199" class="ax_default box_1">
        <div id="u199_div" class=""></div>
        <div id="u199_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u200" class="ax_default box_1">
        <div id="u200_div" class=""></div>
        <div id="u200_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u201" class="ax_default box_1">
        <div id="u201_div" class=""></div>
        <div id="u201_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u185" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u202" class="ax_default" data-left="1665" data-top="2461" data-width="107" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u203" class="ax_default _文本">
          <div id="u203_div" class="" tabindex="0"></div>
          <div id="u203_text" class="text ">
            <p><span>授信详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u204" class="ax_default icon">
          <img id="u204_img" class="img " src="images/授信订单详情/regen/u204.svg">
          <div id="u204_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u205" class="ax_default" data-left="1691" data-top="2773" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u206" class="ax_default line">
          <img id="u206_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u206_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u207" class="ax_default box_2">
          <div id="u207_div" class=""></div>
          <div id="u207_text" class="text ">
            <p><span>股东信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u208" class="ax_default" data-left="1692" data-top="3278" data-width="362" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u209" class="ax_default _文本">
          <div id="u209_div" class=""></div>
          <div id="u209_text" class="text ">
            <p><span>客户证件号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u210" class="ax_default _文本">
          <div id="u210_div" class=""></div>
          <div id="u210_text" class="text ">
            <p><span>110102197901021234</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u211" class="ax_default" data-left="2273" data-top="3038" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u212" class="ax_default _文本">
          <div id="u212_div" class=""></div>
          <div id="u212_text" class="text ">
            <p><span>姓名</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u213" class="ax_default _文本">
          <div id="u213_div" class=""></div>
          <div id="u213_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u214" class="ax_default" data-left="2273" data-top="3278" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u215" class="ax_default _文本">
          <div id="u215_div" class=""></div>
          <div id="u215_text" class="text ">
            <p><span>性别</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u216" class="ax_default _文本">
          <div id="u216_div" class=""></div>
          <div id="u216_text" class="text ">
            <p><span>男</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u217" class="ax_default" data-left="1724" data-top="3310" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u218" class="ax_default _文本">
          <div id="u218_div" class=""></div>
          <div id="u218_text" class="text ">
            <p><span>民族</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u219" class="ax_default _文本">
          <div id="u219_div" class=""></div>
          <div id="u219_text" class="text ">
            <p><span>汉</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u220" class="ax_default" data-left="2273" data-top="3310" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u221" class="ax_default _文本">
          <div id="u221_div" class=""></div>
          <div id="u221_text" class="text ">
            <p><span>出生日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u222" class="ax_default _文本">
          <div id="u222_div" class=""></div>
          <div id="u222_text" class="text ">
            <p><span>2020-09-01</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u223" class="ax_default" data-left="1724" data-top="3338" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u224" class="ax_default _文本">
          <div id="u224_div" class=""></div>
          <div id="u224_text" class="text ">
            <p><span>住址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u225" class="ax_default _文本">
          <div id="u225_div" class=""></div>
          <div id="u225_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u226" class="ax_default" data-left="2273" data-top="3338" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u227" class="ax_default _文本">
          <div id="u227_div" class=""></div>
          <div id="u227_text" class="text ">
            <p><span>签发机关</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u228" class="ax_default _文本">
          <div id="u228_div" class=""></div>
          <div id="u228_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u229" class="ax_default" data-label="添加" title="未选择任何文件" data-left="2383" data-top="3411" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u230" class="ax_default box_1">
          <img id="u230_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u230_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u231" class="ax_default label">
        <div id="u231_div" class=""></div>
        <div id="u231_text" class="text ">
          <p><span>身份证国徽面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u232" class="ax_default" data-left="1684" data-top="3370" data-width="314" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u233" class="ax_default box_1">
          <div id="u233_div" class=""></div>
          <div id="u233_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u234" class="ax_default box_1">
          <div id="u234_div" class=""></div>
          <div id="u234_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u235" class="ax_default" data-left="2239" data-top="3363" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u236" class="ax_default box_1">
          <div id="u236_div" class=""></div>
          <div id="u236_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u237" class="ax_default box_1">
          <div id="u237_div" class=""></div>
          <div id="u237_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u238" class="ax_default" data-left="1722" data-top="2836" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u239" class="ax_default _文本">
          <div id="u239_div" class=""></div>
          <div id="u239_text" class="text ">
            <p><span>股东类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u240" class="ax_default _文本">
          <div id="u240_div" class=""></div>
          <div id="u240_text" class="text ">
            <p><span>企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u241" class="ax_default" data-left="2273" data-top="2836" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u242" class="ax_default _文本">
          <div id="u242_div" class=""></div>
          <div id="u242_text" class="text ">
            <p><span>企业名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u243" class="ax_default _文本">
          <div id="u243_div" class=""></div>
          <div id="u243_text" class="text ">
            <p><span>xxxxxxxxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u244" class="ax_default" data-left="1722" data-top="2866" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u245" class="ax_default _文本">
          <div id="u245_div" class=""></div>
          <div id="u245_text" class="text ">
            <p><span>法定代表人</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u246" class="ax_default _文本">
          <div id="u246_div" class=""></div>
          <div id="u246_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u247" class="ax_default" data-left="2273" data-top="2866" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u248" class="ax_default _文本">
          <div id="u248_div" class=""></div>
          <div id="u248_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u249" class="ax_default _文本">
          <div id="u249_div" class=""></div>
          <div id="u249_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u250" class="ax_default" data-left="1722" data-top="2896" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u251" class="ax_default _文本">
          <div id="u251_div" class=""></div>
          <div id="u251_text" class="text ">
            <p><span>授权方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u252" class="ax_default _文本">
          <div id="u252_div" class=""></div>
          <div id="u252_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u253" class="ax_default" data-left="1745" data-top="2928" data-width="176" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u254" class="ax_default box_1">
          <img id="u254_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u254_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u255" class="ax_default label">
          <div id="u255_div" class=""></div>
          <div id="u255_text" class="text ">
            <p><span>授权文件</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u256" class="ax_default" data-left="1722" data-top="3038" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u257" class="ax_default _文本">
          <div id="u257_div" class=""></div>
          <div id="u257_text" class="text ">
            <p><span>股东类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u258" class="ax_default _文本">
          <div id="u258_div" class=""></div>
          <div id="u258_text" class="text ">
            <p><span>个人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u259" class="ax_default" data-left="1722" data-top="3068" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u260" class="ax_default _文本">
          <div id="u260_div" class=""></div>
          <div id="u260_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u261" class="ax_default _文本">
          <div id="u261_div" class=""></div>
          <div id="u261_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u262" class="ax_default" data-left="2273" data-top="3068" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u263" class="ax_default _文本">
          <div id="u263_div" class=""></div>
          <div id="u263_text" class="text ">
            <p><span>授权方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u264" class="ax_default _文本">
          <div id="u264_div" class=""></div>
          <div id="u264_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u265" class="ax_default" data-left="1745" data-top="3105" data-width="176" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u266" class="ax_default box_1">
          <img id="u266_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u266_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u267" class="ax_default label">
          <div id="u267_div" class=""></div>
          <div id="u267_text" class="text ">
            <p><span>授权文件</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u268" class="ax_default" data-left="2273" data-top="3218" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u269" class="ax_default _文本">
          <div id="u269_div" class=""></div>
          <div id="u269_text" class="text ">
            <p><span>姓名</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u270" class="ax_default _文本">
          <div id="u270_div" class=""></div>
          <div id="u270_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u271" class="ax_default" data-left="1722" data-top="3218" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u272" class="ax_default _文本">
          <div id="u272_div" class=""></div>
          <div id="u272_text" class="text ">
            <p><span>股东类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u273" class="ax_default _文本">
          <div id="u273_div" class=""></div>
          <div id="u273_text" class="text ">
            <p><span>个人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u274" class="ax_default" data-left="1722" data-top="3248" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u275" class="ax_default _文本">
          <div id="u275_div" class=""></div>
          <div id="u275_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u276" class="ax_default _文本">
          <div id="u276_div" class=""></div>
          <div id="u276_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u277" class="ax_default" data-left="2273" data-top="3248" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u278" class="ax_default _文本">
          <div id="u278_div" class=""></div>
          <div id="u278_text" class="text ">
            <p><span>授权方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u279" class="ax_default _文本">
          <div id="u279_div" class=""></div>
          <div id="u279_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u280" class="ax_default" data-label="添加" title="未选择任何文件" data-left="1841" data-top="3407" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u281" class="ax_default box_1">
          <img id="u281_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u281_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u282" class="ax_default label">
        <div id="u282_div" class=""></div>
        <div id="u282_text" class="text ">
          <p><span>身份证人像面</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u283" class="ax_default box_2">
        <div id="u283_div" class=""></div>
        <div id="u283_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u284" class="ax_default box_1">
        <div id="u284_div" class=""></div>
        <div id="u284_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u285" class="ax_default box_1">
        <div id="u285_div" class=""></div>
        <div id="u285_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u286" class="ax_default box_1">
        <div id="u286_div" class=""></div>
        <div id="u286_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u287" class="ax_default" data-left="5663" data-top="26" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u288" class="ax_default _图片_">
          <img id="u288_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u288_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u289" class="ax_default box_1">
          <div id="u289_div" class=""></div>
          <div id="u289_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u290" class="ax_default _图片_">
          <img id="u290_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u290_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u291" class="ax_default box_1">
          <div id="u291_div" class=""></div>
          <div id="u291_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u292" class="ax_default _图片_">
          <img id="u292_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u292_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u293" class="ax_default box_1">
          <div id="u293_div" class=""></div>
          <div id="u293_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u295" class="ax_default box_1">
        <div id="u295_div" class=""></div>
        <div id="u295_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u296" class="ax_default box_1">
        <div id="u296_div" class=""></div>
        <div id="u296_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u297" class="ax_default" data-left="4717" data-top="71" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u298" class="ax_default box_1">
          <div id="u298_div" class=""></div>
          <div id="u298_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u299" class="ax_default _图片_">
          <img id="u299_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u299_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u300" class="ax_default box_1">
          <div id="u300_div" class=""></div>
          <div id="u300_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u301" class="ax_default box_1">
          <div id="u301_div" class=""></div>
          <div id="u301_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u302" class="ax_default box_1">
        <div id="u302_div" class=""></div>
        <div id="u302_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u303" class="ax_default box_1">
        <div id="u303_div" class=""></div>
        <div id="u303_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u304" class="ax_default box_1">
        <img id="u304_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u304_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u305" class="ax_default box_1">
        <div id="u305_div" class=""></div>
        <div id="u305_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u306" class="ax_default box_1">
        <div id="u306_div" class=""></div>
        <div id="u306_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u307" class="ax_default box_1">
        <div id="u307_div" class=""></div>
        <div id="u307_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u308" class="ax_default box_1">
        <div id="u308_div" class=""></div>
        <div id="u308_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u309" class="ax_default box_1">
        <div id="u309_div" class=""></div>
        <div id="u309_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u310" class="ax_default box_1">
        <div id="u310_div" class=""></div>
        <div id="u310_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u294" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u311" class="ax_default" data-left="4931" data-top="86" data-width="107" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u312" class="ax_default _文本">
          <div id="u312_div" class="" tabindex="0"></div>
          <div id="u312_text" class="text ">
            <p><span>授信详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u313" class="ax_default icon">
          <img id="u313_img" class="img " src="images/授信订单详情/regen/u204.svg">
          <div id="u313_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u314" class="ax_default" data-left="4963" data-top="863" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u315" class="ax_default line">
          <img id="u315_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u315_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u316" class="ax_default box_2">
          <div id="u316_div" class=""></div>
          <div id="u316_text" class="text ">
            <p><span>股东信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u317" class="ax_default" data-left="5551" data-top="340" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u318" class="ax_default _文本">
          <div id="u318_div" class=""></div>
          <div id="u318_text" class="text ">
            <p><span>营业期限</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u319" class="ax_default _文本">
          <div id="u319_div" class=""></div>
          <div id="u319_text" class="text ">
            <p><span>XXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u320" class="ax_default" data-left="5514" data-top="375" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u321" class="ax_default _文本">
          <div id="u321_div" class=""></div>
          <div id="u321_text" class="text ">
            <p><span>详细地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u322" class="ax_default _文本">
          <div id="u322_div" class=""></div>
          <div id="u322_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u323" class="ax_default" data-left="5004" data-top="410" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u324" class="ax_default _文本">
          <div id="u324_div" class=""></div>
          <div id="u324_text" class="text ">
            <p><span>经营范围</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u325" class="ax_default _文本">
          <div id="u325_div" class=""></div>
          <div id="u325_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u326" class="ax_default" data-left="4960" data-top="340" data-width="342" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u327" class="ax_default _文本">
          <div id="u327_div" class=""></div>
          <div id="u327_text" class="text ">
            <p><span>企业成立时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u328" class="ax_default _文本">
          <div id="u328_div" class=""></div>
          <div id="u328_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u329" class="ax_default" data-left="4926" data-top="304" data-width="380" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u330" class="ax_default _文本">
          <div id="u330_div" class=""></div>
          <div id="u330_text" class="text ">
            <p><span>统一社会信用代码证号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u331" class="ax_default _文本">
          <div id="u331_div" class=""></div>
          <div id="u331_text" class="text ">
            <p><span>XX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u332" class="ax_default" data-left="4964" data-top="1441" data-width="362" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u333" class="ax_default _文本">
          <div id="u333_div" class=""></div>
          <div id="u333_text" class="text ">
            <p><span>客户证件号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u334" class="ax_default _文本">
          <div id="u334_div" class=""></div>
          <div id="u334_text" class="text ">
            <p><span>110102197901021234</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u335" class="ax_default" data-left="5545" data-top="1167" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u336" class="ax_default _文本">
          <div id="u336_div" class=""></div>
          <div id="u336_text" class="text ">
            <p><span>姓名</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u337" class="ax_default _文本">
          <div id="u337_div" class=""></div>
          <div id="u337_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u338" class="ax_default" data-left="5551" data-top="305" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u339" class="ax_default _文本">
          <div id="u339_div" class=""></div>
          <div id="u339_text" class="text ">
            <p><span>主体类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u340" class="ax_default _文本">
          <div id="u340_div" class=""></div>
          <div id="u340_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u341" class="ax_default" data-left="5004" data-top="375" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u342" class="ax_default _文本">
          <div id="u342_div" class=""></div>
          <div id="u342_text" class="text ">
            <p><span>注册地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u343" class="ax_default _文本">
          <div id="u343_div" class=""></div>
          <div id="u343_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u344" class="ax_default" data-left="5545" data-top="1441" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u345" class="ax_default _文本">
          <div id="u345_div" class=""></div>
          <div id="u345_text" class="text ">
            <p><span>性别</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u346" class="ax_default _文本">
          <div id="u346_div" class=""></div>
          <div id="u346_text" class="text ">
            <p><span>男</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u347" class="ax_default" data-left="4996" data-top="1473" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u348" class="ax_default _文本">
          <div id="u348_div" class=""></div>
          <div id="u348_text" class="text ">
            <p><span>民族</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u349" class="ax_default _文本">
          <div id="u349_div" class=""></div>
          <div id="u349_text" class="text ">
            <p><span>汉</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u350" class="ax_default" data-left="5545" data-top="1473" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u351" class="ax_default _文本">
          <div id="u351_div" class=""></div>
          <div id="u351_text" class="text ">
            <p><span>出生日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u352" class="ax_default _文本">
          <div id="u352_div" class=""></div>
          <div id="u352_text" class="text ">
            <p><span>2020-09-01</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u353" class="ax_default" data-left="4996" data-top="1501" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u354" class="ax_default _文本">
          <div id="u354_div" class=""></div>
          <div id="u354_text" class="text ">
            <p><span>住址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u355" class="ax_default _文本">
          <div id="u355_div" class=""></div>
          <div id="u355_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u356" class="ax_default" data-left="5545" data-top="1501" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u357" class="ax_default _文本">
          <div id="u357_div" class=""></div>
          <div id="u357_text" class="text ">
            <p><span>签发机关</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u358" class="ax_default _文本">
          <div id="u358_div" class=""></div>
          <div id="u358_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u359" class="ax_default" data-left="5004" data-top="448" data-width="199" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u360" class="ax_default box_1">
          <img id="u360_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u360_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u361" class="ax_default label">
          <div id="u361_div" class=""></div>
          <div id="u361_text" class="text ">
            <p><span>营业执照照片</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u362" class="ax_default" data-label="添加" title="未选择任何文件" data-left="5655" data-top="1574" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u363" class="ax_default box_1">
          <img id="u363_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u363_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u364" class="ax_default label">
        <div id="u364_div" class=""></div>
        <div id="u364_text" class="text ">
          <p><span>身份证国徽面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u365" class="ax_default" data-left="4956" data-top="1533" data-width="314" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u366" class="ax_default box_1">
          <div id="u366_div" class=""></div>
          <div id="u366_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u367" class="ax_default box_1">
          <div id="u367_div" class=""></div>
          <div id="u367_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u368" class="ax_default" data-left="5511" data-top="1526" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u369" class="ax_default box_1">
          <div id="u369_div" class=""></div>
          <div id="u369_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u370" class="ax_default box_1">
          <div id="u370_div" class=""></div>
          <div id="u370_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u371" class="ax_default" data-left="5514" data-top="410" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u372" class="ax_default _文本">
          <div id="u372_div" class=""></div>
          <div id="u372_text" class="text ">
            <p><span>决议方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u373" class="ax_default _文本">
          <div id="u373_div" class=""></div>
          <div id="u373_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u374" class="ax_default" data-left="4994" data-top="934" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u375" class="ax_default _文本">
          <div id="u375_div" class=""></div>
          <div id="u375_text" class="text ">
            <p><span>股东类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u376" class="ax_default _文本">
          <div id="u376_div" class=""></div>
          <div id="u376_text" class="text ">
            <p><span>企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u377" class="ax_default" data-left="5545" data-top="934" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u378" class="ax_default _文本">
          <div id="u378_div" class=""></div>
          <div id="u378_text" class="text ">
            <p><span>企业名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u379" class="ax_default _文本">
          <div id="u379_div" class=""></div>
          <div id="u379_text" class="text ">
            <p><span>xxxxxxxxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u380" class="ax_default" data-left="4994" data-top="964" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u381" class="ax_default _文本">
          <div id="u381_div" class=""></div>
          <div id="u381_text" class="text ">
            <p><span>法定代表人</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u382" class="ax_default _文本">
          <div id="u382_div" class=""></div>
          <div id="u382_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u383" class="ax_default" data-left="5545" data-top="964" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u384" class="ax_default _文本">
          <div id="u384_div" class=""></div>
          <div id="u384_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u385" class="ax_default _文本">
          <div id="u385_div" class=""></div>
          <div id="u385_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u386" class="ax_default" data-left="4994" data-top="994" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u387" class="ax_default _文本">
          <div id="u387_div" class=""></div>
          <div id="u387_text" class="text ">
            <p><span>授权方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u388" class="ax_default _文本">
          <div id="u388_div" class=""></div>
          <div id="u388_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u389" class="ax_default" data-left="5017" data-top="1026" data-width="176" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u390" class="ax_default box_1">
          <img id="u390_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u390_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u391" class="ax_default label">
          <div id="u391_div" class=""></div>
          <div id="u391_text" class="text ">
            <p><span>授权文件</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u392" class="ax_default" data-left="4994" data-top="1167" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u393" class="ax_default _文本">
          <div id="u393_div" class=""></div>
          <div id="u393_text" class="text ">
            <p><span>股东类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u394" class="ax_default _文本">
          <div id="u394_div" class=""></div>
          <div id="u394_text" class="text ">
            <p><span>个人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u395" class="ax_default" data-left="4994" data-top="1197" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u396" class="ax_default _文本">
          <div id="u396_div" class=""></div>
          <div id="u396_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u397" class="ax_default _文本">
          <div id="u397_div" class=""></div>
          <div id="u397_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u398" class="ax_default" data-left="5545" data-top="1197" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u399" class="ax_default _文本">
          <div id="u399_div" class=""></div>
          <div id="u399_text" class="text ">
            <p><span>授权方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u400" class="ax_default _文本">
          <div id="u400_div" class=""></div>
          <div id="u400_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u401" class="ax_default" data-left="5017" data-top="1234" data-width="176" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u402" class="ax_default box_1">
          <img id="u402_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u402_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u403" class="ax_default label">
          <div id="u403_div" class=""></div>
          <div id="u403_text" class="text ">
            <p><span>授权文件</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u404" class="ax_default" data-left="5545" data-top="1381" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u405" class="ax_default _文本">
          <div id="u405_div" class=""></div>
          <div id="u405_text" class="text ">
            <p><span>姓名</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u406" class="ax_default _文本">
          <div id="u406_div" class=""></div>
          <div id="u406_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u407" class="ax_default" data-left="4994" data-top="1381" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u408" class="ax_default _文本">
          <div id="u408_div" class=""></div>
          <div id="u408_text" class="text ">
            <p><span>股东类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u409" class="ax_default _文本">
          <div id="u409_div" class=""></div>
          <div id="u409_text" class="text ">
            <p><span>个人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u410" class="ax_default" data-left="4994" data-top="1411" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u411" class="ax_default _文本">
          <div id="u411_div" class=""></div>
          <div id="u411_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u412" class="ax_default _文本">
          <div id="u412_div" class=""></div>
          <div id="u412_text" class="text ">
            <p><span>13001011212</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u413" class="ax_default" data-left="5545" data-top="1411" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u414" class="ax_default _文本">
          <div id="u414_div" class=""></div>
          <div id="u414_text" class="text ">
            <p><span>授权方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u415" class="ax_default _文本">
          <div id="u415_div" class=""></div>
          <div id="u415_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u416" class="ax_default" data-label="添加" title="未选择任何文件" data-left="5113" data-top="1570" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u417" class="ax_default box_1">
          <img id="u417_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u417_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u418" class="ax_default label">
        <div id="u418_div" class=""></div>
        <div id="u418_text" class="text ">
          <p><span>身份证人像面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u419" class="ax_default" data-left="5000" data-top="274" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u420" class="ax_default _文本">
          <div id="u420_div" class=""></div>
          <div id="u420_text" class="text ">
            <p><span>关联人类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u421" class="ax_default _文本">
          <div id="u421_div" class=""></div>
          <div id="u421_text" class="text ">
            <p><span>企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u422" class="ax_default" data-left="5551" data-top="274" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u423" class="ax_default _文本">
          <div id="u423_div" class=""></div>
          <div id="u423_text" class="text ">
            <p><span>关系类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u424" class="ax_default _文本">
          <div id="u424_div" class=""></div>
          <div id="u424_text" class="text ">
            <p><span>抵押人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u425" class="ax_default" data-left="4963" data-top="549" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u426" class="ax_default line">
          <img id="u426_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u426_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u427" class="ax_default box_2">
          <div id="u427_div" class=""></div>
          <div id="u427_text" class="text ">
            <p><span>法定代表人信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u428" class="ax_default" data-left="5012" data-top="612" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u429" class="ax_default _文本">
          <div id="u429_div" class=""></div>
          <div id="u429_text" class="text ">
            <p><span>法定代表人</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u430" class="ax_default _文本">
          <div id="u430_div" class=""></div>
          <div id="u430_text" class="text ">
            <p><span>xxxxxxxxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u431" class="ax_default" data-left="4937" data-top="647" data-width="380" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u432" class="ax_default _文本">
          <div id="u432_div" class=""></div>
          <div id="u432_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u433" class="ax_default _文本">
          <div id="u433_div" class=""></div>
          <div id="u433_text" class="text ">
            <p><span>XX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u434" class="ax_default" data-left="5557" data-top="612" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u435" class="ax_default _文本">
          <div id="u435_div" class=""></div>
          <div id="u435_text" class="text ">
            <p><span>身份证号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u436" class="ax_default _文本">
          <div id="u436_div" class=""></div>
          <div id="u436_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u437" class="ax_default" data-left="5557" data-top="647" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u438" class="ax_default _文本">
          <div id="u438_div" class=""></div>
          <div id="u438_text" class="text ">
            <p><span>性别</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u439" class="ax_default _文本">
          <div id="u439_div" class=""></div>
          <div id="u439_text" class="text ">
            <p><span>男</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u440" class="ax_default" data-left="5008" data-top="679" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u441" class="ax_default _文本">
          <div id="u441_div" class=""></div>
          <div id="u441_text" class="text ">
            <p><span>民族</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u442" class="ax_default _文本">
          <div id="u442_div" class=""></div>
          <div id="u442_text" class="text ">
            <p><span>汉</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u443" class="ax_default" data-left="5557" data-top="679" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u444" class="ax_default _文本">
          <div id="u444_div" class=""></div>
          <div id="u444_text" class="text ">
            <p><span>出生日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u445" class="ax_default _文本">
          <div id="u445_div" class=""></div>
          <div id="u445_text" class="text ">
            <p><span>2020-09-01</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u446" class="ax_default" data-left="5008" data-top="707" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u447" class="ax_default _文本">
          <div id="u447_div" class=""></div>
          <div id="u447_text" class="text ">
            <p><span>住址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u448" class="ax_default _文本">
          <div id="u448_div" class=""></div>
          <div id="u448_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u449" class="ax_default" data-left="5557" data-top="707" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u450" class="ax_default _文本">
          <div id="u450_div" class=""></div>
          <div id="u450_text" class="text ">
            <p><span>签发机关</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u451" class="ax_default _文本">
          <div id="u451_div" class=""></div>
          <div id="u451_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u452" class="ax_default" data-label="添加" title="未选择任何文件" data-left="5667" data-top="780" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u453" class="ax_default box_1">
          <img id="u453_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u453_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u454" class="ax_default label">
        <div id="u454_div" class=""></div>
        <div id="u454_text" class="text ">
          <p><span>身份证国徽面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u455" class="ax_default" data-left="4968" data-top="739" data-width="314" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u456" class="ax_default box_1">
          <div id="u456_div" class=""></div>
          <div id="u456_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u457" class="ax_default box_1">
          <div id="u457_div" class=""></div>
          <div id="u457_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u458" class="ax_default" data-left="5523" data-top="732" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u459" class="ax_default box_1">
          <div id="u459_div" class=""></div>
          <div id="u459_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u460" class="ax_default box_1">
          <div id="u460_div" class=""></div>
          <div id="u460_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u461" class="ax_default" data-label="添加" title="未选择任何文件" data-left="5125" data-top="776" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u462" class="ax_default box_1">
          <img id="u462_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u462_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u463" class="ax_default label">
        <div id="u463_div" class=""></div>
        <div id="u463_text" class="text ">
          <p><span>身份证人像面</span></p>
        </div>
      </div>

      <!-- Unnamed (Image) -->
      <div id="u464" class="ax_default _图片_">
        <img id="u464_img" class="img " src="images/授信订单详情/regen/u464.png">
        <div id="u464_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Image) -->
      <div id="u465" class="ax_default _图片_">
        <img id="u465_img" class="img " src="images/授信订单详情/regen/u465.png">
        <div id="u465_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u466" class="ax_default box_2">
        <div id="u466_div" class=""></div>
        <div id="u466_text" class="text ">
          <p><span>王小明</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u467" class="ax_default box_2">
        <div id="u467_div" class=""></div>
        <div id="u467_text" class="text ">
          <p><span>平原县信誉金店</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u468" class="ax_default" data-left="4994" data-top="1768" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u469" class="ax_default _文本">
          <div id="u469_div" class=""></div>
          <div id="u469_text" class="text ">
            <p><span>关联人类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u470" class="ax_default _文本">
          <div id="u470_div" class=""></div>
          <div id="u470_text" class="text ">
            <p><span>个人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u471" class="ax_default" data-left="5545" data-top="1768" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u472" class="ax_default _文本">
          <div id="u472_div" class=""></div>
          <div id="u472_text" class="text ">
            <p><span>关系类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u473" class="ax_default _文本">
          <div id="u473_div" class=""></div>
          <div id="u473_text" class="text ">
            <p><span>配偶/法定代表人/抵押人</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u474" class="ax_default" data-left="1722" data-top="3021" data-width="905" data-height="1">

        <!-- Unnamed (Line) -->
        <div id="u475" class="ax_default line">
          <img id="u475_img" class="img " src="images/授信订单详情/regen/u475.svg">
          <div id="u475_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u476" class="ax_default" data-left="1722" data-top="3199" data-width="905" data-height="1">

        <!-- Unnamed (Line) -->
        <div id="u477" class="ax_default line">
          <img id="u477_img" class="img " src="images/授信订单详情/regen/u475.svg">
          <div id="u477_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u478" class="ax_default" data-left="5000" data-top="2132" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u479" class="ax_default _文本">
          <div id="u479_div" class=""></div>
          <div id="u479_text" class="text ">
            <p><span>企业名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u480" class="ax_default _文本">
          <div id="u480_div" class=""></div>
          <div id="u480_text" class="text ">
            <p><span>xxxxxxxxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u481" class="ax_default" data-left="5545" data-top="2167" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u482" class="ax_default _文本">
          <div id="u482_div" class=""></div>
          <div id="u482_text" class="text ">
            <p><span>营业期限</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u483" class="ax_default _文本">
          <div id="u483_div" class=""></div>
          <div id="u483_text" class="text ">
            <p><span>XXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u484" class="ax_default" data-left="4963" data-top="2237" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u485" class="ax_default _文本">
          <div id="u485_div" class=""></div>
          <div id="u485_text" class="text ">
            <p><span>详细地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u486" class="ax_default _文本">
          <div id="u486_div" class=""></div>
          <div id="u486_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u487" class="ax_default" data-left="5545" data-top="2237" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u488" class="ax_default _文本">
          <div id="u488_div" class=""></div>
          <div id="u488_text" class="text ">
            <p><span>经营范围</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u489" class="ax_default _文本">
          <div id="u489_div" class=""></div>
          <div id="u489_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u490" class="ax_default" data-left="4963" data-top="2202" data-width="342" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u491" class="ax_default _文本">
          <div id="u491_div" class=""></div>
          <div id="u491_text" class="text ">
            <p><span>企业成立时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u492" class="ax_default _文本">
          <div id="u492_div" class=""></div>
          <div id="u492_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u493" class="ax_default" data-left="4925" data-top="2167" data-width="380" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u494" class="ax_default _文本">
          <div id="u494_div" class=""></div>
          <div id="u494_text" class="text ">
            <p><span>统一社会信用代码证号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u495" class="ax_default _文本">
          <div id="u495_div" class=""></div>
          <div id="u495_text" class="text ">
            <p><span>XX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u496" class="ax_default" data-left="5545" data-top="2132" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u497" class="ax_default _文本">
          <div id="u497_div" class=""></div>
          <div id="u497_text" class="text ">
            <p><span>主体类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u498" class="ax_default _文本">
          <div id="u498_div" class=""></div>
          <div id="u498_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u499" class="ax_default" data-left="5545" data-top="2202" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u500" class="ax_default _文本">
          <div id="u500_div" class=""></div>
          <div id="u500_text" class="text ">
            <p><span>注册地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u501" class="ax_default _文本">
          <div id="u501_div" class=""></div>
          <div id="u501_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u502" class="ax_default" data-left="4997" data-top="2302" data-width="199" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u503" class="ax_default box_1">
          <img id="u503_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u503_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u504" class="ax_default label">
          <div id="u504_div" class=""></div>
          <div id="u504_text" class="text ">
            <p><span>营业执照照片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u505" class="ax_default" data-left="4963" data-top="2267" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u506" class="ax_default _文本">
          <div id="u506_div" class=""></div>
          <div id="u506_text" class="text ">
            <p><span>决议方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u507" class="ax_default _文本">
          <div id="u507_div" class=""></div>
          <div id="u507_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u508" class="ax_default" data-left="5467" data-top="1804" data-width="380" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u509" class="ax_default _文本">
          <div id="u509_div" class=""></div>
          <div id="u509_text" class="text ">
            <p><span>手机号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u510" class="ax_default _文本">
          <div id="u510_div" class=""></div>
          <div id="u510_text" class="text ">
            <p><span>XX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u511" class="ax_default" data-left="4994" data-top="1804" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u512" class="ax_default _文本">
          <div id="u512_div" class=""></div>
          <div id="u512_text" class="text ">
            <p><span>身份证号码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u513" class="ax_default _文本">
          <div id="u513_div" class=""></div>
          <div id="u513_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u514" class="ax_default" data-left="4996" data-top="1842" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u515" class="ax_default _文本">
          <div id="u515_div" class=""></div>
          <div id="u515_text" class="text ">
            <p><span>性别</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u516" class="ax_default _文本">
          <div id="u516_div" class=""></div>
          <div id="u516_text" class="text ">
            <p><span>男</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u517" class="ax_default" data-left="5545" data-top="1842" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u518" class="ax_default _文本">
          <div id="u518_div" class=""></div>
          <div id="u518_text" class="text ">
            <p><span>民族</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u519" class="ax_default _文本">
          <div id="u519_div" class=""></div>
          <div id="u519_text" class="text ">
            <p><span>汉</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u520" class="ax_default" data-left="4996" data-top="1872" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u521" class="ax_default _文本">
          <div id="u521_div" class=""></div>
          <div id="u521_text" class="text ">
            <p><span>出生日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u522" class="ax_default _文本">
          <div id="u522_div" class=""></div>
          <div id="u522_text" class="text ">
            <p><span>2020-09-01</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u523" class="ax_default" data-left="5545" data-top="1868" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u524" class="ax_default _文本">
          <div id="u524_div" class=""></div>
          <div id="u524_text" class="text ">
            <p><span>住址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u525" class="ax_default _文本">
          <div id="u525_div" class=""></div>
          <div id="u525_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u526" class="ax_default" data-left="4996" data-top="1904" data-width="302" data-height="18">

        <!-- Unnamed (Rectangle) -->
        <div id="u527" class="ax_default _文本">
          <div id="u527_div" class=""></div>
          <div id="u527_text" class="text ">
            <p><span>签发机关</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u528" class="ax_default _文本">
          <div id="u528_div" class=""></div>
          <div id="u528_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u529" class="ax_default" data-label="添加" title="未选择任何文件" data-left="5655" data-top="1975" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u530" class="ax_default box_1">
          <img id="u530_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u530_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u531" class="ax_default label">
        <div id="u531_div" class=""></div>
        <div id="u531_text" class="text ">
          <p><span>身份证国徽面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u532" class="ax_default" data-left="5511" data-top="1893" data-width="314" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u533" class="ax_default box_1">
          <div id="u533_div" class=""></div>
          <div id="u533_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u534" class="ax_default box_1">
          <div id="u534_div" class=""></div>
          <div id="u534_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u535" class="ax_default" data-left="4963" data-top="1934" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u536" class="ax_default box_1">
          <div id="u536_div" class=""></div>
          <div id="u536_text" class="text ">
            <p><span>身份证有效开始日期</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u537" class="ax_default box_1">
          <div id="u537_div" class=""></div>
          <div id="u537_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u538" class="ax_default" data-label="添加" title="未选择任何文件" data-left="5113" data-top="1971" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u539" class="ax_default box_1">
          <img id="u539_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u539_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u540" class="ax_default label">
        <div id="u540_div" class=""></div>
        <div id="u540_text" class="text ">
          <p><span>身份证人像面</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u541" class="ax_default" data-left="4963" data-top="2068" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u542" class="ax_default line">
          <img id="u542_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u542_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u543" class="ax_default box_2">
          <div id="u543_div" class=""></div>
          <div id="u543_text" class="text ">
            <p><span>关联企业信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Image) -->
      <div id="u544" class="ax_default _图片_">
        <img id="u544_img" class="img " src="images/授信订单详情/regen/u464.png">
        <div id="u544_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u545" class="ax_default box_2">
        <div id="u545_div" class=""></div>
        <div id="u545_text" class="text ">
          <p><span>李四</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u546" class="ax_default box_2">
        <div id="u546_div" class=""></div>
        <div id="u546_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u547" class="ax_default box_1">
        <div id="u547_div" class=""></div>
        <div id="u547_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u548" class="ax_default box_1">
        <div id="u548_div" class=""></div>
        <div id="u548_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u549" class="ax_default box_1">
        <div id="u549_div" class=""></div>
        <div id="u549_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u550" class="ax_default" data-left="7145" data-top="41" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u551" class="ax_default _图片_">
          <img id="u551_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u551_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u552" class="ax_default box_1">
          <div id="u552_div" class=""></div>
          <div id="u552_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u553" class="ax_default _图片_">
          <img id="u553_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u553_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u554" class="ax_default box_1">
          <div id="u554_div" class=""></div>
          <div id="u554_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u555" class="ax_default _图片_">
          <img id="u555_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u555_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u556" class="ax_default box_1">
          <div id="u556_div" class=""></div>
          <div id="u556_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u558" class="ax_default box_1">
        <div id="u558_div" class=""></div>
        <div id="u558_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u559" class="ax_default box_1">
        <div id="u559_div" class=""></div>
        <div id="u559_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u560" class="ax_default" data-left="6199" data-top="86" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u561" class="ax_default box_1">
          <div id="u561_div" class=""></div>
          <div id="u561_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u562" class="ax_default _图片_">
          <img id="u562_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u562_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u563" class="ax_default box_1">
          <div id="u563_div" class=""></div>
          <div id="u563_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u564" class="ax_default box_1">
          <div id="u564_div" class=""></div>
          <div id="u564_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u565" class="ax_default box_1">
        <div id="u565_div" class=""></div>
        <div id="u565_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u566" class="ax_default box_1">
        <div id="u566_div" class=""></div>
        <div id="u566_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u567" class="ax_default box_1">
        <img id="u567_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u567_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u568" class="ax_default box_1">
        <div id="u568_div" class=""></div>
        <div id="u568_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u569" class="ax_default box_1">
        <div id="u569_div" class=""></div>
        <div id="u569_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u570" class="ax_default box_1">
        <div id="u570_div" class=""></div>
        <div id="u570_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u571" class="ax_default box_1">
        <div id="u571_div" class=""></div>
        <div id="u571_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u572" class="ax_default box_1">
        <div id="u572_div" class=""></div>
        <div id="u572_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u573" class="ax_default box_1">
        <div id="u573_div" class=""></div>
        <div id="u573_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u557" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u574" class="ax_default" data-left="6413" data-top="101" data-width="107" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u575" class="ax_default _文本">
          <div id="u575_div" class="" tabindex="0"></div>
          <div id="u575_text" class="text ">
            <p><span>授信详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u576" class="ax_default icon">
          <img id="u576_img" class="img " src="images/授信订单详情/regen/u204.svg">
          <div id="u576_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Table) -->
      <div id="u577" class="ax_default">

        <!-- Unnamed (Table Cell) -->
        <div id="u578" class="ax_default table_cell">
          <img id="u578_img" class="img " src="images/授信订单详情/regen/u578.png">
          <div id="u578_text" class="text ">
            <p><span>文件名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u579" class="ax_default table_cell">
          <img id="u579_img" class="img " src="images/授信订单详情/regen/u579.png">
          <div id="u579_text" class="text ">
            <p><span>文件</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u580" class="ax_default table_cell">
          <img id="u580_img" class="img " src="images/授信订单详情/regen/u580.png">
          <div id="u580_text" class="text ">
            <p><span>产品配置的下户补件</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u581" class="ax_default table_cell">
          <img id="u581_img" class="img " src="images/授信订单详情/regen/u581.png">
          <div id="u581_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u582" class="ax_default table_cell">
          <img id="u582_img" class="img " src="images/授信订单详情/regen/u582.png">
          <div id="u582_text" class="text ">
            <p><span>产品配置的出账补件</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u583" class="ax_default table_cell">
          <img id="u583_img" class="img " src="images/授信订单详情/regen/u583.png">
          <div id="u583_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u584" class="ax_default" data-label="添加" title="未选择任何文件" data-left="7018" data-top="340" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u585" class="ax_default box_1">
          <img id="u585_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u585_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- 添加 (Group) -->
      <div id="u586" class="ax_default" data-label="添加" title="未选择任何文件" data-left="7018" data-top="489" data-width="80" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u587" class="ax_default box_1">
          <img id="u587_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u587_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u588" class="ax_default" data-left="5017" data-top="1132" data-width="905" data-height="1">

        <!-- Unnamed (Line) -->
        <div id="u589" class="ax_default line">
          <img id="u589_img" class="img " src="images/授信订单详情/regen/u475.svg">
          <div id="u589_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u590" class="ax_default" data-left="5017" data-top="1350" data-width="905" data-height="1">

        <!-- Unnamed (Line) -->
        <div id="u591" class="ax_default line">
          <img id="u591_img" class="img " src="images/授信订单详情/regen/u475.svg">
          <div id="u591_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u592" class="ax_default" data-left="778" data-top="1679" data-width="365" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u593" class="ax_default _文本">
          <div id="u593_div" class=""></div>
          <div id="u593_text" class="text ">
            <p><span>额度失效时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u594" class="ax_default _文本">
          <div id="u594_div" class=""></div>
          <div id="u594_text" class="text ">
            <p><span>2022-01-02</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u595" class="ax_default box_2">
        <div id="u595_div" class=""></div>
        <div id="u595_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u596" class="ax_default box_1">
        <div id="u596_div" class=""></div>
        <div id="u596_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u597" class="ax_default box_1">
        <div id="u597_div" class=""></div>
        <div id="u597_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u598" class="ax_default box_1">
        <div id="u598_div" class=""></div>
        <div id="u598_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u599" class="ax_default" data-left="4033" data-top="45" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u600" class="ax_default _图片_">
          <img id="u600_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u600_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u601" class="ax_default box_1">
          <div id="u601_div" class=""></div>
          <div id="u601_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u602" class="ax_default _图片_">
          <img id="u602_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u602_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u603" class="ax_default box_1">
          <div id="u603_div" class=""></div>
          <div id="u603_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u604" class="ax_default _图片_">
          <img id="u604_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u604_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u605" class="ax_default box_1">
          <div id="u605_div" class=""></div>
          <div id="u605_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u607" class="ax_default box_1">
        <div id="u607_div" class=""></div>
        <div id="u607_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u608" class="ax_default box_1">
        <div id="u608_div" class=""></div>
        <div id="u608_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u609" class="ax_default" data-left="3087" data-top="90" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u610" class="ax_default box_1">
          <div id="u610_div" class=""></div>
          <div id="u610_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u611" class="ax_default _图片_">
          <img id="u611_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u611_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u612" class="ax_default box_1">
          <div id="u612_div" class=""></div>
          <div id="u612_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u613" class="ax_default box_1">
          <div id="u613_div" class=""></div>
          <div id="u613_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u614" class="ax_default box_1">
        <div id="u614_div" class=""></div>
        <div id="u614_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u615" class="ax_default box_1">
        <div id="u615_div" class=""></div>
        <div id="u615_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u616" class="ax_default box_1">
        <img id="u616_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u616_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u617" class="ax_default box_1">
        <div id="u617_div" class=""></div>
        <div id="u617_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u618" class="ax_default box_1">
        <div id="u618_div" class=""></div>
        <div id="u618_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u619" class="ax_default box_1">
        <div id="u619_div" class=""></div>
        <div id="u619_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u620" class="ax_default box_1">
        <div id="u620_div" class=""></div>
        <div id="u620_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u621" class="ax_default box_1">
        <div id="u621_div" class=""></div>
        <div id="u621_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u622" class="ax_default box_1">
        <div id="u622_div" class=""></div>
        <div id="u622_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u606" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u623" class="ax_default" data-left="3301" data-top="105" data-width="141" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u624" class="ax_default _文本">
          <div id="u624_div" class="" tabindex="0"></div>
          <div id="u624_text" class="text ">
            <p><span>授信订单详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u625" class="ax_default icon">
          <img id="u625_img" class="img " src="images/授信订单详情/regen/u30.svg">
          <div id="u625_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u626" class="ax_default" data-left="3376" data-top="258" data-width="313" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u627" class="ax_default box_1">
          <div id="u627_div" class=""></div>
          <div id="u627_text" class="text ">
            <p><span>抵押人</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u628" class="ax_default box_1">
          <div id="u628_div" class=""></div>
          <div id="u628_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u629" class="ax_default" data-left="3925" data-top="258" data-width="320" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u630" class="ax_default box_1">
          <div id="u630_div" class=""></div>
          <div id="u630_text" class="text ">
            <p><span>押品类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u631" class="ax_default box_1">
          <div id="u631_div" class=""></div>
          <div id="u631_text" class="text ">
            <p><span>抵押物</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u632" class="ax_default" data-left="3376" data-top="295" data-width="265" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u633" class="ax_default box_1">
          <div id="u633_div" class=""></div>
          <div id="u633_text" class="text ">
            <p><span>财产类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u634" class="ax_default box_1">
          <div id="u634_div" class=""></div>
          <div id="u634_text" class="text ">
            <p><span>住房</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u635" class="ax_default" data-left="3943" data-top="295" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u636" class="ax_default box_1">
          <div id="u636_div" class=""></div>
          <div id="u636_text" class="text ">
            <p><span>详细地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u637" class="ax_default box_1">
          <div id="u637_div" class=""></div>
          <div id="u637_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u638" class="ax_default" data-left="3407" data-top="330" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u639" class="ax_default box_1">
          <div id="u639_div" class=""></div>
          <div id="u639_text" class="text ">
            <p><span>物业类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u640" class="ax_default box_1">
          <img id="u640_img" class="img " src="images/授信订单详情/regen/u640.svg">
          <div id="u640_text" class="text ">
            <p><span>住宅</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u641" class="ax_default" data-left="3894" data-top="330" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u642" class="ax_default box_1">
          <div id="u642_div" class=""></div>
          <div id="u642_text" class="text ">
            <p><span>房屋面积(m²)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u643" class="ax_default box_1">
          <div id="u643_div" class=""></div>
          <div id="u643_text" class="text ">
            <p><span>100</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u644" class="ax_default" data-left="3391" data-top="365" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u645" class="ax_default box_1">
          <div id="u645_div" class=""></div>
          <div id="u645_text" class="text ">
            <p><span>总楼层</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u646" class="ax_default box_1">
          <img id="u646_img" class="img " src="images/授信订单详情/regen/u646.svg">
          <div id="u646_text" class="text ">
            <p><span>20</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u647" class="ax_default" data-left="3894" data-top="365" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u648" class="ax_default box_1">
          <div id="u648_div" class=""></div>
          <div id="u648_text" class="text ">
            <p><span>所在楼层</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u649" class="ax_default box_1">
          <div id="u649_div" class=""></div>
          <div id="u649_text" class="text ">
            <p><span>10</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u650" class="ax_default" data-left="3372" data-top="453" data-width="313" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u651" class="ax_default box_1">
          <div id="u651_div" class=""></div>
          <div id="u651_text" class="text ">
            <p><span>抵押人</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u652" class="ax_default box_1">
          <div id="u652_div" class=""></div>
          <div id="u652_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u653" class="ax_default" data-left="3921" data-top="453" data-width="320" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u654" class="ax_default box_1">
          <div id="u654_div" class=""></div>
          <div id="u654_text" class="text ">
            <p><span>押品类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u655" class="ax_default box_1">
          <div id="u655_div" class=""></div>
          <div id="u655_text" class="text ">
            <p><span>抵押物</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u656" class="ax_default" data-left="3372" data-top="490" data-width="265" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u657" class="ax_default box_1">
          <div id="u657_div" class=""></div>
          <div id="u657_text" class="text ">
            <p><span>财产类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u658" class="ax_default box_1">
          <div id="u658_div" class=""></div>
          <div id="u658_text" class="text ">
            <p><span>厂房</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u659" class="ax_default" data-left="3909" data-top="490" data-width="332" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u660" class="ax_default box_1">
          <div id="u660_div" class=""></div>
          <div id="u660_text" class="text ">
            <p><span>财产描述</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u661" class="ax_default box_1">
          <div id="u661_div" class=""></div>
          <div id="u661_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u662" class="ax_default" data-left="3394" data-top="528" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u663" class="ax_default box_1">
          <div id="u663_div" class=""></div>
          <div id="u663_text" class="text ">
            <p><span>财产价值</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u664" class="ax_default box_1">
          <div id="u664_div" class=""></div>
          <div id="u664_text" class="text ">
            <p><span>12000999</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u665" class="ax_default" data-left="3921" data-top="528" data-width="272" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u666" class="ax_default box_1">
          <div id="u666_div" class=""></div>
          <div id="u666_text" class="text ">
            <p><span>押品添加时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u667" class="ax_default box_1">
          <img id="u667_img" class="img " src="images/授信订单详情/regen/u667.svg">
          <div id="u667_text" class="text ">
            <p><span>2023-01-05</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u668" class="ax_default" data-left="3391" data-top="563" data-width="199" data-height="80">

        <!-- 添加 (Group) -->
        <div id="u669" class="ax_default" data-label="添加" title="未选择任何文件" data-left="3510" data-top="563" data-width="80" data-height="80">

          <!-- Unnamed (Rectangle) -->
          <div id="u670" class="ax_default box_1">
            <img id="u670_img" class="img " src="images/授信订单详情/regen/u125.svg">
            <div id="u670_text" class="text ">
              <p><span>图片</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u671" class="ax_default label">
          <div id="u671_div" class=""></div>
          <div id="u671_text" class="text ">
            <p><span>押品照片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u672" class="ax_default" data-left="3431" data-top="417" data-width="905" data-height="1">

        <!-- Unnamed (Line) -->
        <div id="u673" class="ax_default line">
          <img id="u673_img" class="img " src="images/授信订单详情/regen/u475.svg">
          <div id="u673_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u674" class="ax_default" data-left="289" data-top="1071" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u675" class="ax_default _文本">
          <div id="u675_div" class=""></div>
          <div id="u675_text" class="text ">
            <p><span>企业名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u676" class="ax_default _文本">
          <div id="u676_div" class=""></div>
          <div id="u676_text" class="text ">
            <p><span>xxxxxxxxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u677" class="ax_default" data-left="834" data-top="1106" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u678" class="ax_default _文本">
          <div id="u678_div" class=""></div>
          <div id="u678_text" class="text ">
            <p><span>营业期限</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u679" class="ax_default _文本">
          <div id="u679_div" class=""></div>
          <div id="u679_text" class="text ">
            <p><span>XXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u680" class="ax_default" data-left="252" data-top="1176" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u681" class="ax_default _文本">
          <div id="u681_div" class=""></div>
          <div id="u681_text" class="text ">
            <p><span>详细地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u682" class="ax_default _文本">
          <div id="u682_div" class=""></div>
          <div id="u682_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u683" class="ax_default" data-left="834" data-top="1176" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u684" class="ax_default _文本">
          <div id="u684_div" class=""></div>
          <div id="u684_text" class="text ">
            <p><span>经营范围</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u685" class="ax_default _文本">
          <div id="u685_div" class=""></div>
          <div id="u685_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u686" class="ax_default" data-left="252" data-top="1141" data-width="342" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u687" class="ax_default _文本">
          <div id="u687_div" class=""></div>
          <div id="u687_text" class="text ">
            <p><span>企业成立时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u688" class="ax_default _文本">
          <div id="u688_div" class=""></div>
          <div id="u688_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u689" class="ax_default" data-left="214" data-top="1106" data-width="380" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u690" class="ax_default _文本">
          <div id="u690_div" class=""></div>
          <div id="u690_text" class="text ">
            <p><span>统一社会信用代码证号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u691" class="ax_default _文本">
          <div id="u691_div" class=""></div>
          <div id="u691_text" class="text ">
            <p><span>XX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u692" class="ax_default" data-left="834" data-top="1071" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u693" class="ax_default _文本">
          <div id="u693_div" class=""></div>
          <div id="u693_text" class="text ">
            <p><span>主体类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u694" class="ax_default _文本">
          <div id="u694_div" class=""></div>
          <div id="u694_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u695" class="ax_default" data-left="834" data-top="1141" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u696" class="ax_default _文本">
          <div id="u696_div" class=""></div>
          <div id="u696_text" class="text ">
            <p><span>注册地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u697" class="ax_default _文本">
          <div id="u697_div" class=""></div>
          <div id="u697_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u698" class="ax_default" data-left="286" data-top="1241" data-width="199" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u699" class="ax_default box_1">
          <img id="u699_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u699_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u700" class="ax_default label">
          <div id="u700_div" class=""></div>
          <div id="u700_text" class="text ">
            <p><span>营业执照照片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u701" class="ax_default" data-left="252" data-top="1206" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u702" class="ax_default _文本">
          <div id="u702_div" class=""></div>
          <div id="u702_text" class="text ">
            <p><span>决议方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u703" class="ax_default _文本">
          <div id="u703_div" class=""></div>
          <div id="u703_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Table) -->
      <div id="u704" class="ax_default">

        <!-- Unnamed (Table Cell) -->
        <div id="u705" class="ax_default table_cell">
          <img id="u705_img" class="img " src="images/授信订单详情/regen/u705.png">
          <div id="u705_text" class="text ">
            <p><span>操作人</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u706" class="ax_default table_cell">
          <img id="u706_img" class="img " src="images/授信订单详情/regen/u706.png">
          <div id="u706_text" class="text ">
            <p><span>操作时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u707" class="ax_default table_cell">
          <img id="u707_img" class="img " src="images/授信订单详情/regen/u707.png">
          <div id="u707_text" class="text ">
            <p><span>授信环节</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u708" class="ax_default table_cell">
          <img id="u708_img" class="img " src="images/授信订单详情/regen/u708.png">
          <div id="u708_text" class="text ">
            <p><span>当前授信结论</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u709" class="ax_default table_cell">
          <img id="u709_img" class="img " src="images/授信订单详情/regen/u709.png">
          <div id="u709_text" class="text ">
            <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">{</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">客户姓名</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">}</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u710" class="ax_default table_cell">
          <img id="u710_img" class="img " src="images/授信订单详情/regen/u710.png">
          <div id="u710_text" class="text ">
            <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">2020-09-01 hh</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">mm</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">ss</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u711" class="ax_default table_cell">
          <img id="u711_img" class="img " src="images/授信订单详情/regen/u711.png">
          <div id="u711_text" class="text ">
            <p><span>贷款申请</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u712" class="ax_default table_cell">
          <img id="u712_img" class="img " src="images/授信订单详情/regen/u712.png">
          <div id="u712_text" class="text ">
            <p><span>提交申请，客户经理贷前尽调未完成，请联系客户经理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u713" class="ax_default" data-left="1665" data-top="2500" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u714" class="ax_default box_21">
          <div id="u714_div" class=""></div>
          <div id="u714_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u715" class="ax_default" data-left="1703" data-top="2500" data-width="723" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u716" class="ax_default box_21">
            <div id="u716_div" class=""></div>
            <div id="u716_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u717" class="ax_default box_21">
            <div id="u717_div" class=""></div>
            <div id="u717_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u718" class="ax_default box_21">
            <div id="u718_div" class=""></div>
            <div id="u718_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u719" class="ax_default box_21">
            <div id="u719_div" class=""></div>
            <div id="u719_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u720" class="ax_default box_21">
            <div id="u720_div" class=""></div>
            <div id="u720_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u721" class="ax_default" data-left="3301" data-top="129" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u722" class="ax_default box_21">
          <div id="u722_div" class=""></div>
          <div id="u722_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u723" class="ax_default" data-left="3339" data-top="129" data-width="723" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u724" class="ax_default box_21">
            <div id="u724_div" class=""></div>
            <div id="u724_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u725" class="ax_default box_21">
            <div id="u725_div" class=""></div>
            <div id="u725_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u726" class="ax_default box_21">
            <div id="u726_div" class=""></div>
            <div id="u726_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u727" class="ax_default box_21">
            <div id="u727_div" class=""></div>
            <div id="u727_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u728" class="ax_default box_21">
            <div id="u728_div" class=""></div>
            <div id="u728_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u729" class="ax_default" data-left="4937" data-top="129" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u730" class="ax_default box_21">
          <div id="u730_div" class=""></div>
          <div id="u730_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u731" class="ax_default" data-left="4975" data-top="129" data-width="723" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u732" class="ax_default box_21">
            <div id="u732_div" class=""></div>
            <div id="u732_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u733" class="ax_default box_21">
            <div id="u733_div" class=""></div>
            <div id="u733_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u734" class="ax_default box_21">
            <div id="u734_div" class=""></div>
            <div id="u734_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u735" class="ax_default box_21">
            <div id="u735_div" class=""></div>
            <div id="u735_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u736" class="ax_default box_21">
            <div id="u736_div" class=""></div>
            <div id="u736_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u737" class="ax_default" data-left="6413" data-top="129" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u738" class="ax_default box_21">
          <div id="u738_div" class=""></div>
          <div id="u738_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u739" class="ax_default" data-left="6451" data-top="129" data-width="734" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u740" class="ax_default box_21">
            <div id="u740_div" class=""></div>
            <div id="u740_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u741" class="ax_default box_21">
            <div id="u741_div" class=""></div>
            <div id="u741_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u742" class="ax_default box_21">
            <div id="u742_div" class=""></div>
            <div id="u742_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u743" class="ax_default box_21">
            <div id="u743_div" class=""></div>
            <div id="u743_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u744" class="ax_default box_21">
            <div id="u744_div" class=""></div>
            <div id="u744_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u745" class="ax_default" data-left="807" data-top="1577" data-width="336" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u746" class="ax_default _文本">
          <div id="u746_div" class=""></div>
          <div id="u746_text" class="text ">
            <p><span>是否循环授信</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u747" class="ax_default _文本">
          <div id="u747_div" class=""></div>
          <div id="u747_text" class="text ">
            <p><span>是</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u748" class="ax_default" data-left="792" data-top="1613" data-width="351" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u749" class="ax_default _文本">
          <div id="u749_div" class=""></div>
          <div id="u749_text" class="text ">
            <p><span>多年期授信利率(%)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u750" class="ax_default _文本">
          <div id="u750_div" class=""></div>
          <div id="u750_text" class="text ">
            <p><span>12</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u751" class="ax_default box_2">
        <div id="u751_div" class=""></div>
        <div id="u751_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u752" class="ax_default box_1">
        <div id="u752_div" class=""></div>
        <div id="u752_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u753" class="ax_default box_1">
        <div id="u753_div" class=""></div>
        <div id="u753_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u754" class="ax_default box_1">
        <div id="u754_div" class=""></div>
        <div id="u754_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u755" class="ax_default" data-left="957" data-top="2405" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u756" class="ax_default _图片_">
          <img id="u756_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u756_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u757" class="ax_default box_1">
          <div id="u757_div" class=""></div>
          <div id="u757_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u758" class="ax_default _图片_">
          <img id="u758_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u758_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u759" class="ax_default box_1">
          <div id="u759_div" class=""></div>
          <div id="u759_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u760" class="ax_default _图片_">
          <img id="u760_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u760_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u761" class="ax_default box_1">
          <div id="u761_div" class=""></div>
          <div id="u761_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u763" class="ax_default box_1">
        <div id="u763_div" class=""></div>
        <div id="u763_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u764" class="ax_default box_1">
        <div id="u764_div" class=""></div>
        <div id="u764_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u765" class="ax_default" data-left="11" data-top="2450" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u766" class="ax_default box_1">
          <div id="u766_div" class=""></div>
          <div id="u766_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u767" class="ax_default _图片_">
          <img id="u767_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u767_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u768" class="ax_default box_1">
          <div id="u768_div" class=""></div>
          <div id="u768_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u769" class="ax_default box_1">
          <div id="u769_div" class=""></div>
          <div id="u769_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u770" class="ax_default box_1">
        <div id="u770_div" class=""></div>
        <div id="u770_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u771" class="ax_default box_1">
        <div id="u771_div" class=""></div>
        <div id="u771_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u772" class="ax_default box_1">
        <img id="u772_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u772_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u773" class="ax_default box_1">
        <div id="u773_div" class=""></div>
        <div id="u773_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u774" class="ax_default box_1">
        <div id="u774_div" class=""></div>
        <div id="u774_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u775" class="ax_default box_1">
        <div id="u775_div" class=""></div>
        <div id="u775_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u776" class="ax_default box_1">
        <div id="u776_div" class=""></div>
        <div id="u776_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u777" class="ax_default box_1">
        <div id="u777_div" class=""></div>
        <div id="u777_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u778" class="ax_default box_1">
        <div id="u778_div" class=""></div>
        <div id="u778_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u762" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u779" class="ax_default" data-left="225" data-top="2465" data-width="141" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u780" class="ax_default _文本">
          <div id="u780_div" class="" tabindex="0"></div>
          <div id="u780_text" class="text ">
            <p><span>授信订单详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u781" class="ax_default icon">
          <img id="u781_img" class="img " src="images/授信订单详情/regen/u30.svg">
          <div id="u781_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u782" class="ax_default" data-left="300" data-top="2623" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u783" class="ax_default _文本">
          <div id="u783_div" class=""></div>
          <div id="u783_text" class="text ">
            <p><span>授信申请编号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u784" class="ax_default _文本">
          <div id="u784_div" class=""></div>
          <div id="u784_text" class="text ">
            <p><span>DL20221010000001</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u785" class="ax_default" data-left="845" data-top="2658" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u786" class="ax_default _文本">
          <div id="u786_div" class=""></div>
          <div id="u786_text" class="text ">
            <p><span>产品名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u787" class="ax_default _文本">
          <div id="u787_div" class=""></div>
          <div id="u787_text" class="text ">
            <p><span>XXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u788" class="ax_default" data-left="263" data-top="2728" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u789" class="ax_default _文本">
          <div id="u789_div" class=""></div>
          <div id="u789_text" class="text ">
            <p><span>申请金额(元)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u790" class="ax_default _文本">
          <div id="u790_div" class=""></div>
          <div id="u790_text" class="text ">
            <p><span>100,000.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u791" class="ax_default" data-left="845" data-top="2728" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u792" class="ax_default _文本">
          <div id="u792_div" class=""></div>
          <div id="u792_text" class="text ">
            <p><span>申请期限(月)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u793" class="ax_default _文本">
          <div id="u793_div" class=""></div>
          <div id="u793_text" class="text ">
            <p><span>3</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u794" class="ax_default" data-left="852" data-top="2763" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u795" class="ax_default _文本">
          <div id="u795_div" class=""></div>
          <div id="u795_text" class="text ">
            <p><span>还款方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u796" class="ax_default _文本">
          <div id="u796_div" class=""></div>
          <div id="u796_text" class="text ">
            <p><span>等额本息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u797" class="ax_default" data-left="300" data-top="2763" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u798" class="ax_default _文本">
          <div id="u798_div" class=""></div>
          <div id="u798_text" class="text ">
            <p><span>贷款用途</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u799" class="ax_default _文本">
          <div id="u799_div" class=""></div>
          <div id="u799_text" class="text ">
            <p><span>日常经营</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u800" class="ax_default" data-left="826" data-top="2798" data-width="328" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u801" class="ax_default _文本">
          <div id="u801_div" class=""></div>
          <div id="u801_text" class="text ">
            <p><span>客户经理</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u802" class="ax_default _文本">
          <div id="u802_div" class=""></div>
          <div id="u802_text" class="text ">
            <p><span>吴帆</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u803" class="ax_default" data-left="303" data-top="2693" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u804" class="ax_default _文本">
          <div id="u804_div" class=""></div>
          <div id="u804_text" class="text ">
            <p><span>担保方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u805" class="ax_default _文本">
          <div id="u805_div" class=""></div>
          <div id="u805_text" class="text ">
            <p><span>抵押</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u806" class="ax_default" data-left="852" data-top="2833" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u807" class="ax_default _文本">
          <div id="u807_div" class=""></div>
          <div id="u807_text" class="text ">
            <p><span>申请时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u808" class="ax_default _文本">
          <div id="u808_div" class=""></div>
          <div id="u808_text" class="text ">
            <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">2020-09-01 hh</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">mm</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">ss</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u809" class="ax_default" data-left="303" data-top="2833" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u810" class="ax_default _文本">
          <div id="u810_div" class=""></div>
          <div id="u810_text" class="text ">
            <p><span>授信状态</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u811" class="ax_default _文本">
          <div id="u811_div" class=""></div>
          <div id="u811_text" class="text ">
            <p><span>授信拒绝</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u812" class="ax_default" data-left="260" data-top="2970" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u813" class="ax_default line">
          <img id="u813_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u813_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u814" class="ax_default box_2">
          <div id="u814_div" class=""></div>
          <div id="u814_text" class="text ">
            <p><span>授信主体信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u815" class="ax_default" data-left="303" data-top="2658" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u816" class="ax_default _文本">
          <div id="u816_div" class=""></div>
          <div id="u816_text" class="text ">
            <p><span>渠道来源</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u817" class="ax_default _文本">
          <div id="u817_div" class=""></div>
          <div id="u817_text" class="text ">
            <p><span>XX渠道</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u818" class="ax_default" data-left="260" data-top="3321" data-width="1110" data-height="304">

        <!-- Unnamed (Group) -->
        <div id="u819" class="ax_default" data-left="260" data-top="3321" data-width="1110" data-height="44">

          <!-- Unnamed (Line) -->
          <div id="u820" class="ax_default line">
            <img id="u820_img" class="img " src="images/授信订单详情/regen/u32.svg">
            <div id="u820_text" class="text " style="display:none; visibility: hidden">
              <p></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u821" class="ax_default box_2">
            <div id="u821_div" class=""></div>
            <div id="u821_text" class="text ">
              <p><span>法代信息</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u822" class="ax_default" data-left="818" data-top="3379" data-width="362" data-height="20">

          <!-- Unnamed (Rectangle) -->
          <div id="u823" class="ax_default _文本">
            <div id="u823_div" class=""></div>
            <div id="u823_text" class="text ">
              <p><span>证件号码</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u824" class="ax_default _文本">
            <div id="u824_div" class=""></div>
            <div id="u824_text" class="text ">
              <p><span>110102197901021234</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u825" class="ax_default" data-left="300" data-top="3379" data-width="302" data-height="20">

          <!-- Unnamed (Rectangle) -->
          <div id="u826" class="ax_default _文本">
            <div id="u826_div" class=""></div>
            <div id="u826_text" class="text ">
              <p><span>姓名</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u827" class="ax_default _文本">
            <div id="u827_div" class=""></div>
            <div id="u827_text" class="text ">
              <p><span>张三</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u828" class="ax_default" data-left="300" data-top="3412" data-width="302" data-height="20">

          <!-- Unnamed (Rectangle) -->
          <div id="u829" class="ax_default _文本">
            <div id="u829_div" class=""></div>
            <div id="u829_text" class="text ">
              <p><span>手机号码</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u830" class="ax_default _文本">
            <div id="u830_div" class=""></div>
            <div id="u830_text" class="text ">
              <p><span>13001011212</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u831" class="ax_default" data-left="849" data-top="3412" data-width="302" data-height="20">

          <!-- Unnamed (Rectangle) -->
          <div id="u832" class="ax_default _文本">
            <div id="u832_div" class=""></div>
            <div id="u832_text" class="text ">
              <p><span>性别</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u833" class="ax_default _文本">
            <div id="u833_div" class=""></div>
            <div id="u833_text" class="text ">
              <p><span>男</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u834" class="ax_default" data-left="300" data-top="3444" data-width="302" data-height="20">

          <!-- Unnamed (Rectangle) -->
          <div id="u835" class="ax_default _文本">
            <div id="u835_div" class=""></div>
            <div id="u835_text" class="text ">
              <p><span>民族</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u836" class="ax_default _文本">
            <div id="u836_div" class=""></div>
            <div id="u836_text" class="text ">
              <p><span>汉</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u837" class="ax_default" data-left="849" data-top="3444" data-width="302" data-height="18">

          <!-- Unnamed (Rectangle) -->
          <div id="u838" class="ax_default _文本">
            <div id="u838_div" class=""></div>
            <div id="u838_text" class="text ">
              <p><span>出生日期</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u839" class="ax_default _文本">
            <div id="u839_div" class=""></div>
            <div id="u839_text" class="text ">
              <p><span>2020-09-01</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u840" class="ax_default" data-left="300" data-top="3472" data-width="302" data-height="20">

          <!-- Unnamed (Rectangle) -->
          <div id="u841" class="ax_default _文本">
            <div id="u841_div" class=""></div>
            <div id="u841_text" class="text ">
              <p><span>住址</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u842" class="ax_default _文本">
            <div id="u842_div" class=""></div>
            <div id="u842_text" class="text ">
              <p><span>xxxxxx</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u843" class="ax_default" data-left="849" data-top="3472" data-width="302" data-height="18">

          <!-- Unnamed (Rectangle) -->
          <div id="u844" class="ax_default _文本">
            <div id="u844_div" class=""></div>
            <div id="u844_text" class="text ">
              <p><span>签发机关</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u845" class="ax_default _文本">
            <div id="u845_div" class=""></div>
            <div id="u845_text" class="text ">
              <p><span>xxxx</span></p>
            </div>
          </div>
        </div>

        <!-- 添加 (Group) -->
        <div id="u846" class="ax_default" data-label="添加" title="未选择任何文件" data-left="414" data-top="3540" data-width="80" data-height="80">

          <!-- Unnamed (Rectangle) -->
          <div id="u847" class="ax_default box_1">
            <img id="u847_img" class="img " src="images/授信订单详情/regen/u125.svg">
            <div id="u847_text" class="text ">
              <p><span>图片</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u848" class="ax_default label">
          <div id="u848_div" class=""></div>
          <div id="u848_text" class="text ">
            <p><span>身份证人像面</span></p>
          </div>
        </div>

        <!-- 添加 (Group) -->
        <div id="u849" class="ax_default" data-label="添加" title="未选择任何文件" data-left="959" data-top="3545" data-width="80" data-height="80">

          <!-- Unnamed (Rectangle) -->
          <div id="u850" class="ax_default box_1">
            <img id="u850_img" class="img " src="images/授信订单详情/regen/u125.svg">
            <div id="u850_text" class="text ">
              <p><span>图片</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u851" class="ax_default label">
          <div id="u851_div" class=""></div>
          <div id="u851_text" class="text ">
            <p><span>身份证国徽面</span></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u852" class="ax_default" data-left="260" data-top="3504" data-width="314" data-height="25">

          <!-- Unnamed (Rectangle) -->
          <div id="u853" class="ax_default box_1">
            <div id="u853_div" class=""></div>
            <div id="u853_text" class="text ">
              <p><span>身份证有效开始日期</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u854" class="ax_default box_1">
            <div id="u854_div" class=""></div>
            <div id="u854_text" class="text ">
              <p><span>XXXXXXXXXXXXX</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u855" class="ax_default" data-left="815" data-top="3497" data-width="319" data-height="25">

          <!-- Unnamed (Rectangle) -->
          <div id="u856" class="ax_default box_1">
            <div id="u856_div" class=""></div>
            <div id="u856_text" class="text ">
              <p><span>身份证有效开始日期</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u857" class="ax_default box_1">
            <div id="u857_div" class=""></div>
            <div id="u857_text" class="text ">
              <p><span>XXXXXXXXXXXXX</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u858" class="ax_default" data-left="845" data-top="2623" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u859" class="ax_default _文本">
          <div id="u859_div" class=""></div>
          <div id="u859_text" class="text ">
            <p><span>网贷申请编号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u860" class="ax_default _文本">
          <div id="u860_div" class=""></div>
          <div id="u860_text" class="text ">
            <p><span>DL20221010000001</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u861" class="ax_default" data-left="845" data-top="2693" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u862" class="ax_default _文本">
          <div id="u862_div" class=""></div>
          <div id="u862_text" class="text ">
            <p><span>授信主体</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u863" class="ax_default _文本">
          <div id="u863_div" class=""></div>
          <div id="u863_text" class="text ">
            <p><span>企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u864" class="ax_default" data-left="274" data-top="2798" data-width="328" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u865" class="ax_default _文本">
          <div id="u865_div" class=""></div>
          <div id="u865_text" class="text ">
            <p><span>申请机构</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u866" class="ax_default _文本">
          <div id="u866_div" class=""></div>
          <div id="u866_text" class="text ">
            <p><span>10,000.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u867" class="ax_default" data-left="300" data-top="4486" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u868" class="ax_default _文本">
          <div id="u868_div" class=""></div>
          <div id="u868_text" class="text ">
            <p><span>额度状态</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u869" class="ax_default _文本">
          <div id="u869_div" class=""></div>
          <div id="u869_text" class="text ">
            <p><span>-</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u870" class="ax_default" data-left="263" data-top="4288" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u871" class="ax_default line">
          <img id="u871_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u871_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u872" class="ax_default box_2">
          <div id="u872_div" class=""></div>
          <div id="u872_text" class="text ">
            <p><span>额度信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u873" class="ax_default" data-left="263" data-top="4355" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u874" class="ax_default _文本">
          <div id="u874_div" class=""></div>
          <div id="u874_text" class="text ">
            <p><span>授信额度(元)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u875" class="ax_default _文本">
          <div id="u875_div" class=""></div>
          <div id="u875_text" class="text ">
            <p><span>100,000.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u876" class="ax_default" data-left="300" data-top="4424" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u877" class="ax_default _文本">
          <div id="u877_div" class=""></div>
          <div id="u877_text" class="text ">
            <p><span>授信期限(月)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u878" class="ax_default _文本">
          <div id="u878_div" class=""></div>
          <div id="u878_text" class="text ">
            <p><span>3</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u879" class="ax_default" data-left="852" data-top="4424" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u880" class="ax_default _文本">
          <div id="u880_div" class=""></div>
          <div id="u880_text" class="text ">
            <p><span>还款方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u881" class="ax_default _文本">
          <div id="u881_div" class=""></div>
          <div id="u881_text" class="text ">
            <p><span>等额本息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u882" class="ax_default" data-left="257" data-top="4391" data-width="351" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u883" class="ax_default _文本">
          <div id="u883_div" class=""></div>
          <div id="u883_text" class="text ">
            <p><span>1年期授信利率(%)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u884" class="ax_default _文本">
          <div id="u884_div" class=""></div>
          <div id="u884_text" class="text ">
            <p><span>12</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u885" class="ax_default" data-left="237" data-top="4454" data-width="365" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u886" class="ax_default _文本">
          <div id="u886_div" class=""></div>
          <div id="u886_text" class="text ">
            <p><span>额度生效时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u887" class="ax_default _文本">
          <div id="u887_div" class=""></div>
          <div id="u887_text" class="text ">
            <p><span>2022-01-02</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u888" class="ax_default" data-left="225" data-top="2519" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u889" class="ax_default box_21">
          <div id="u889_div" class=""></div>
          <div id="u889_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u890" class="ax_default" data-left="274" data-top="2519" data-width="712" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u891" class="ax_default box_21">
            <div id="u891_div" class=""></div>
            <div id="u891_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u892" class="ax_default box_21">
            <div id="u892_div" class=""></div>
            <div id="u892_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u893" class="ax_default box_21">
            <div id="u893_div" class=""></div>
            <div id="u893_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u894" class="ax_default box_21">
            <div id="u894_div" class=""></div>
            <div id="u894_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u895" class="ax_default box_21">
            <div id="u895_div" class=""></div>
            <div id="u895_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u896" class="ax_default" data-left="251" data-top="4542" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u897" class="ax_default line">
          <img id="u897_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u897_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u898" class="ax_default box_2">
          <div id="u898_div" class=""></div>
          <div id="u898_text" class="text ">
            <p><span>进度详情</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u899" class="ax_default" data-left="303" data-top="2868" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u900" class="ax_default _文本">
          <div id="u900_div" class=""></div>
          <div id="u900_text" class="text ">
            <p><span>业务模式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u901" class="ax_default _文本">
          <div id="u901_div" class=""></div>
          <div id="u901_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u902" class="ax_default" data-left="852" data-top="2868" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u903" class="ax_default _文本">
          <div id="u903_div" class=""></div>
          <div id="u903_text" class="text ">
            <p><span>所属商户</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u904" class="ax_default _文本">
          <div id="u904_div" class=""></div>
          <div id="u904_text" class="text ">
            <p><span>xxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u905" class="ax_default" data-left="222" data-top="2898" data-width="383" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u906" class="ax_default _文本">
          <div id="u906_div" class=""></div>
          <div id="u906_text" class="text ">
            <p><span>是否指定担保公司</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u907" class="ax_default _文本">
          <div id="u907_div" class=""></div>
          <div id="u907_text" class="text ">
            <p><span>是</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u908" class="ax_default" data-left="771" data-top="2898" data-width="383" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u909" class="ax_default _文本">
          <div id="u909_div" class=""></div>
          <div id="u909_text" class="text ">
            <p><span>担保公司</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u910" class="ax_default _文本">
          <div id="u910_div" class=""></div>
          <div id="u910_text" class="text ">
            <p><span>xx公司</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u911" class="ax_default" data-left="322" data-top="3713" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u912" class="ax_default box_1">
          <div id="u912_div" class=""></div>
          <div id="u912_text" class="text ">
            <p><span>支付方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u913" class="ax_default box_1">
          <div id="u913_div" class=""></div>
          <div id="u913_text" class="text ">
            <p><span>受托支付</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u914" class="ax_default" data-left="829" data-top="3742" data-width="366" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u915" class="ax_default box_1">
          <div id="u915_div" class=""></div>
          <div id="u915_text" class="text ">
            <p><span>账号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u916" class="ax_default box_1">
          <div id="u916_div" class=""></div>
          <div id="u916_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u917" class="ax_default" data-left="301" data-top="3738" data-width="319" data-height="32">

        <!-- Unnamed (Rectangle) -->
        <div id="u918" class="ax_default box_1">
          <div id="u918_div" class=""></div>
          <div id="u918_text" class="text ">
            <p><span>账号名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u919" class="ax_default box_1">
          <div id="u919_div" class=""></div>
          <div id="u919_text" class="text ">
            <p><span>XXXXXXX企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u920" class="ax_default" data-left="809" data-top="3772" data-width="368" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u921" class="ax_default box_1">
          <div id="u921_div" class=""></div>
          <div id="u921_text" class="text ">
            <p><span>开户行行名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u922" class="ax_default box_1">
          <div id="u922_div" class=""></div>
          <div id="u922_text" class="text ">
            <p><span>威海银行济南支行</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u923" class="ax_default" data-left="292" data-top="3775" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u924" class="ax_default box_1">
          <div id="u924_div" class=""></div>
          <div id="u924_text" class="text ">
            <p><span>开户行行号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u925" class="ax_default box_1">
          <div id="u925_div" class=""></div>
          <div id="u925_text" class="text ">
            <p><span>12000999</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u926" class="ax_default" data-left="190" data-top="3811" data-width="425" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u927" class="ax_default box_1">
          <div id="u927_div" class=""></div>
          <div id="u927_text" class="text ">
            <p><span>受托支付额度(元)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u928" class="ax_default box_1">
          <div id="u928_div" class=""></div>
          <div id="u928_text" class="text ">
            <p><span>100.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u929" class="ax_default" data-left="829" data-top="3713" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u930" class="ax_default box_1">
          <div id="u930_div" class=""></div>
          <div id="u930_text" class="text ">
            <p><span>借款用途</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u931" class="ax_default box_1">
          <div id="u931_div" class=""></div>
          <div id="u931_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u932" class="ax_default" data-left="766" data-top="3811" data-width="362" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u933" class="ax_default box_1">
          <div id="u933_div" class=""></div>
          <div id="u933_text" class="text ">
            <p><span>受托支付是否行内标识</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u934" class="ax_default box_1">
          <div id="u934_div" class=""></div>
          <div id="u934_text" class="text ">
            <p><span>是</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u935" class="ax_default" data-left="834" data-top="3848" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u936" class="ax_default box_1">
          <div id="u936_div" class=""></div>
          <div id="u936_text" class="text ">
            <p><span>结束时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u937" class="ax_default box_1">
          <div id="u937_div" class=""></div>
          <div id="u937_text" class="text ">
            <p><span>2023-01-05</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u938" class="ax_default" data-left="330" data-top="3848" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u939" class="ax_default box_1">
          <div id="u939_div" class=""></div>
          <div id="u939_text" class="text ">
            <p><span>开始时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u940" class="ax_default box_1">
          <div id="u940_div" class=""></div>
          <div id="u940_text" class="text ">
            <p><span>2023-01-05</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u941" class="ax_default" data-left="263" data-top="3653" data-width="1110" data-height="44">

        <!-- Unnamed (Line) -->
        <div id="u942" class="ax_default line">
          <img id="u942_img" class="img " src="images/授信订单详情/regen/u32.svg">
          <div id="u942_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u943" class="ax_default box_2">
          <div id="u943_div" class=""></div>
          <div id="u943_text" class="text ">
            <p><span>支付信息</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u944" class="ax_default" data-left="237" data-top="3887" data-width="269" data-height="80">

        <!-- 添加 (Group) -->
        <div id="u945" class="ax_default" data-label="添加" title="未选择任何文件" data-left="426" data-top="3887" data-width="80" data-height="80">

          <!-- Unnamed (Rectangle) -->
          <div id="u946" class="ax_default box_1">
            <img id="u946_img" class="img " src="images/授信订单详情/regen/u125.svg">
            <div id="u946_text" class="text ">
              <p><span>图片</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u947" class="ax_default label">
          <div id="u947_div" class=""></div>
          <div id="u947_text" class="text ">
            <p><span>受托支付证明材料</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u948" class="ax_default" data-left="789" data-top="4457" data-width="365" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u949" class="ax_default _文本">
          <div id="u949_div" class=""></div>
          <div id="u949_text" class="text ">
            <p><span>额度失效时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u950" class="ax_default _文本">
          <div id="u950_div" class=""></div>
          <div id="u950_text" class="text ">
            <p><span>2022-01-02</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u951" class="ax_default" data-left="297" data-top="3046" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u952" class="ax_default _文本">
          <div id="u952_div" class=""></div>
          <div id="u952_text" class="text ">
            <p><span>客户名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u953" class="ax_default _文本">
          <div id="u953_div" class=""></div>
          <div id="u953_text" class="text ">
            <p><span>茅台股份有限公司</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u954" class="ax_default" data-left="842" data-top="3081" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u955" class="ax_default _文本">
          <div id="u955_div" class=""></div>
          <div id="u955_text" class="text ">
            <p><span>营业期限</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u956" class="ax_default _文本">
          <div id="u956_div" class=""></div>
          <div id="u956_text" class="text ">
            <p><span>XXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u957" class="ax_default" data-left="260" data-top="3151" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u958" class="ax_default _文本">
          <div id="u958_div" class=""></div>
          <div id="u958_text" class="text ">
            <p><span>详细地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u959" class="ax_default _文本">
          <div id="u959_div" class=""></div>
          <div id="u959_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u960" class="ax_default" data-left="842" data-top="3151" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u961" class="ax_default _文本">
          <div id="u961_div" class=""></div>
          <div id="u961_text" class="text ">
            <p><span>经营范围</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u962" class="ax_default _文本">
          <div id="u962_div" class=""></div>
          <div id="u962_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u963" class="ax_default" data-left="260" data-top="3116" data-width="342" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u964" class="ax_default _文本">
          <div id="u964_div" class=""></div>
          <div id="u964_text" class="text ">
            <p><span>企业成立时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u965" class="ax_default _文本">
          <div id="u965_div" class=""></div>
          <div id="u965_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u966" class="ax_default" data-left="222" data-top="3081" data-width="380" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u967" class="ax_default _文本">
          <div id="u967_div" class=""></div>
          <div id="u967_text" class="text ">
            <p><span>统一社会信用代码证号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u968" class="ax_default _文本">
          <div id="u968_div" class=""></div>
          <div id="u968_text" class="text ">
            <p><span>XX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u969" class="ax_default" data-left="842" data-top="3046" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u970" class="ax_default _文本">
          <div id="u970_div" class=""></div>
          <div id="u970_text" class="text ">
            <p><span>主体类型</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u971" class="ax_default _文本">
          <div id="u971_div" class=""></div>
          <div id="u971_text" class="text ">
            <p><span>xxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u972" class="ax_default" data-left="842" data-top="3116" data-width="302" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u973" class="ax_default _文本">
          <div id="u973_div" class=""></div>
          <div id="u973_text" class="text ">
            <p><span>注册地址</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u974" class="ax_default _文本">
          <div id="u974_div" class=""></div>
          <div id="u974_text" class="text ">
            <p><span>xxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u975" class="ax_default" data-left="294" data-top="3216" data-width="199" data-height="80">

        <!-- Unnamed (Rectangle) -->
        <div id="u976" class="ax_default box_1">
          <img id="u976_img" class="img " src="images/授信订单详情/regen/u125.svg">
          <div id="u976_text" class="text ">
            <p><span>图片</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u977" class="ax_default label">
          <div id="u977_div" class=""></div>
          <div id="u977_text" class="text ">
            <p><span>营业执照照片</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u978" class="ax_default" data-left="260" data-top="3181" data-width="339" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u979" class="ax_default _文本">
          <div id="u979_div" class=""></div>
          <div id="u979_text" class="text ">
            <p><span>决议方式</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u980" class="ax_default _文本">
          <div id="u980_div" class=""></div>
          <div id="u980_text" class="text ">
            <p><span>xxxxxxx</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Table) -->
      <div id="u981" class="ax_default">

        <!-- Unnamed (Table Cell) -->
        <div id="u982" class="ax_default table_cell">
          <img id="u982_img" class="img " src="images/授信订单详情/regen/u705.png">
          <div id="u982_text" class="text ">
            <p><span>操作人</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u983" class="ax_default table_cell">
          <img id="u983_img" class="img " src="images/授信订单详情/regen/u706.png">
          <div id="u983_text" class="text ">
            <p><span>操作时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u984" class="ax_default table_cell">
          <img id="u984_img" class="img " src="images/授信订单详情/regen/u707.png">
          <div id="u984_text" class="text ">
            <p><span>授信环节</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u985" class="ax_default table_cell">
          <img id="u985_img" class="img " src="images/授信订单详情/regen/u708.png">
          <div id="u985_text" class="text ">
            <p><span>当前授信结论</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u986" class="ax_default table_cell">
          <img id="u986_img" class="img " src="images/授信订单详情/regen/u709.png">
          <div id="u986_text" class="text ">
            <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">{</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">客户姓名</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">}</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u987" class="ax_default table_cell">
          <img id="u987_img" class="img " src="images/授信订单详情/regen/u710.png">
          <div id="u987_text" class="text ">
            <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">2020-09-01 hh</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">mm</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">：</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">ss</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u988" class="ax_default table_cell">
          <img id="u988_img" class="img " src="images/授信订单详情/regen/u711.png">
          <div id="u988_text" class="text ">
            <p><span>贷款申请</span></p>
          </div>
        </div>

        <!-- Unnamed (Table Cell) -->
        <div id="u989" class="ax_default table_cell">
          <img id="u989_img" class="img " src="images/授信订单详情/regen/u712.png">
          <div id="u989_text" class="text ">
            <p><span>提交申请，客户经理贷前尽调未完成，请联系客户经理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u990" class="ax_default" data-left="818" data-top="4355" data-width="336" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u991" class="ax_default _文本">
          <div id="u991_div" class=""></div>
          <div id="u991_text" class="text ">
            <p><span>是否循环授信</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u992" class="ax_default _文本">
          <div id="u992_div" class=""></div>
          <div id="u992_text" class="text ">
            <p><span>是</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u993" class="ax_default" data-left="803" data-top="4391" data-width="351" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u994" class="ax_default _文本">
          <div id="u994_div" class=""></div>
          <div id="u994_text" class="text ">
            <p><span>多年期授信利率(%)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u995" class="ax_default _文本">
          <div id="u995_div" class=""></div>
          <div id="u995_text" class="text ">
            <p><span>12</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Ellipse) -->
      <div id="u996" class="ax_default ellipse">
        <img id="u996_img" class="img " src="images/授信订单详情/regen/u996.svg">
        <div id="u996_text" class="text ">
          <p><span>？</span></p>
        </div>
      </div>

      <!-- Unnamed (Speech Bubble) -->
      <div id="u997" class="ax_default _形状">
        <img id="u997_img" class="img " src="images/授信订单详情/regen/u997.svg">
        <div id="u997_text" class="text ">
          <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">{</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">拒绝原因</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">}</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u998" class="ax_default _标题_1">
        <div id="u998_div" class=""></div>
        <div id="u998_text" class="text ">
          <p><span>申请信息：授信主体-个人</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u999" class="ax_default _标题_1">
        <div id="u999_div" class=""></div>
        <div id="u999_text" class="text ">
          <p><span>申请信息：授信主体-企业</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1000" class="ax_default box_2">
        <div id="u1000_div" class=""></div>
        <div id="u1000_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1001" class="ax_default box_1">
        <div id="u1001_div" class=""></div>
        <div id="u1001_text" class="text ">
          <p><span>LOGO</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1002" class="ax_default box_1">
        <div id="u1002_div" class=""></div>
        <div id="u1002_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1003" class="ax_default box_1">
        <div id="u1003_div" class=""></div>
        <div id="u1003_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1004" class="ax_default" data-left="2440" data-top="105" data-width="355" data-height="30">

        <!-- Unnamed (Image) -->
        <div id="u1005" class="ax_default _图片_">
          <img id="u1005_img" class="img " src="images/授信订单详情/regen/u5.png">
          <div id="u1005_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1006" class="ax_default box_1">
          <div id="u1006_div" class=""></div>
          <div id="u1006_text" class="text ">
            <p><span>Administrator</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u1007" class="ax_default _图片_">
          <img id="u1007_img" class="img " src="images/授信订单详情/regen/u7.png">
          <div id="u1007_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1008" class="ax_default box_1">
          <div id="u1008_div" class=""></div>
          <div id="u1008_text" class="text ">
            <p><span>消息</span></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u1009" class="ax_default _图片_">
          <img id="u1009_img" class="img " src="images/授信订单详情/regen/u9.png">
          <div id="u1009_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1010" class="ax_default box_1">
          <div id="u1010_div" class=""></div>
          <div id="u1010_text" class="text ">
            <p><span>张三</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (菜单) -->

      <!-- Unnamed (Rectangle) -->
      <div id="u1012" class="ax_default box_1">
        <div id="u1012_div" class=""></div>
        <div id="u1012_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1013" class="ax_default box_1">
        <div id="u1013_div" class=""></div>
        <div id="u1013_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1014" class="ax_default" data-left="1494" data-top="150" data-width="200" data-height="40">

        <!-- Unnamed (Rectangle) -->
        <div id="u1015" class="ax_default box_1">
          <div id="u1015_div" class=""></div>
          <div id="u1015_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Image) -->
        <div id="u1016" class="ax_default _图片_">
          <img id="u1016_img" class="img " src="images/授信订单详情/regen/u16.png">
          <div id="u1016_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1017" class="ax_default box_1">
          <div id="u1017_div" class=""></div>
          <div id="u1017_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1018" class="ax_default box_1">
          <div id="u1018_div" class=""></div>
          <div id="u1018_text" class="text ">
            <p><span>订单管理</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1019" class="ax_default box_1">
        <div id="u1019_div" class=""></div>
        <div id="u1019_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1020" class="ax_default box_1">
        <div id="u1020_div" class=""></div>
        <div id="u1020_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Shape) -->
      <div id="u1021" class="ax_default box_1">
        <img id="u1021_img" class="img " src="images/授信订单详情/regen/u21.svg">
        <div id="u1021_text" class="text ">
          <p><span>- 授信管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1022" class="ax_default box_1">
        <div id="u1022_div" class=""></div>
        <div id="u1022_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1023" class="ax_default box_1">
        <div id="u1023_div" class=""></div>
        <div id="u1023_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1024" class="ax_default box_1">
        <div id="u1024_div" class=""></div>
        <div id="u1024_text" class="text ">
          <p><span>- 支用管理</span></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1025" class="ax_default box_1">
        <div id="u1025_div" class=""></div>
        <div id="u1025_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1026" class="ax_default box_1">
        <div id="u1026_div" class=""></div>
        <div id="u1026_text" class="text " style="display:none; visibility: hidden">
          <p></p>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1027" class="ax_default box_1">
        <div id="u1027_div" class=""></div>
        <div id="u1027_text" class="text ">
          <p><span>- 还款管理</span></p>
        </div>
      </div>
      <div id="u1011" style="display:none; visibility:hidden;"></div>

      <!-- Unnamed (Group) -->
      <div id="u1028" class="ax_default" data-left="1708" data-top="165" data-width="107" data-height="24" style="cursor: pointer;">

        <!-- Unnamed (Rectangle) -->
        <div id="u1029" class="ax_default _文本">
          <div id="u1029_div" class="" tabindex="0"></div>
          <div id="u1029_text" class="text ">
            <p><span>授信详情</span></p>
          </div>
        </div>

        <!-- Unnamed (Shape) -->
        <div id="u1030" class="ax_default icon">
          <img id="u1030_img" class="img " src="images/授信订单详情/regen/u204.svg">
          <div id="u1030_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1031" class="ax_default" data-left="1708" data-top="204" data-width="1136" data-height="46">

        <!-- Unnamed (Rectangle) -->
        <div id="u1032" class="ax_default box_21">
          <div id="u1032_div" class=""></div>
          <div id="u1032_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>

        <!-- Unnamed (Group) -->
        <div id="u1033" class="ax_default" data-left="1746" data-top="204" data-width="723" data-height="46">

          <!-- Unnamed (Rectangle) -->
          <div id="u1034" class="ax_default box_21">
            <div id="u1034_div" class=""></div>
            <div id="u1034_text" class="text ">
              <p><span>授信主体详细信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u1035" class="ax_default box_21">
            <div id="u1035_div" class=""></div>
            <div id="u1035_text" class="text ">
              <p><span>申请信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u1036" class="ax_default box_21">
            <div id="u1036_div" class=""></div>
            <div id="u1036_text" class="text ">
              <p><span>关联人信息</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u1037" class="ax_default box_21">
            <div id="u1037_div" class=""></div>
            <div id="u1037_text" class="text ">
              <p><span>补充资料</span></p>
            </div>
          </div>

          <!-- Unnamed (Rectangle) -->
          <div id="u1038" class="ax_default box_21">
            <div id="u1038_div" class=""></div>
            <div id="u1038_text" class="text ">
              <p><span>押品信息</span></p>
            </div>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1039" class="ax_default" data-left="301" data-top="3997" data-width="976" data-height="1">

        <!-- Unnamed (Line) -->
        <div id="u1040" class="ax_default line">
          <img id="u1040_img" class="img " src="images/授信订单详情/regen/u1040.svg">
          <div id="u1040_text" class="text " style="display:none; visibility: hidden">
            <p></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1041" class="ax_default" data-left="829" data-top="4031" data-width="366" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1042" class="ax_default box_1">
          <div id="u1042_div" class=""></div>
          <div id="u1042_text" class="text ">
            <p><span>账号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1043" class="ax_default box_1">
          <div id="u1043_div" class=""></div>
          <div id="u1043_text" class="text ">
            <p><span>XXXXXXXXXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1044" class="ax_default" data-left="301" data-top="4027" data-width="319" data-height="32">

        <!-- Unnamed (Rectangle) -->
        <div id="u1045" class="ax_default box_1">
          <div id="u1045_div" class=""></div>
          <div id="u1045_text" class="text ">
            <p><span>账号名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1046" class="ax_default box_1">
          <div id="u1046_div" class=""></div>
          <div id="u1046_text" class="text ">
            <p><span>XXXXXXX企业</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1047" class="ax_default" data-left="809" data-top="4061" data-width="368" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1048" class="ax_default box_1">
          <div id="u1048_div" class=""></div>
          <div id="u1048_text" class="text ">
            <p><span>开户行行名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1049" class="ax_default box_1">
          <div id="u1049_div" class=""></div>
          <div id="u1049_text" class="text ">
            <p><span>威海银行济南支行</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1050" class="ax_default" data-left="292" data-top="4064" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1051" class="ax_default box_1">
          <div id="u1051_div" class=""></div>
          <div id="u1051_text" class="text ">
            <p><span>开户行行号</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1052" class="ax_default box_1">
          <div id="u1052_div" class=""></div>
          <div id="u1052_text" class="text ">
            <p><span>12000999</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1053" class="ax_default" data-left="190" data-top="4100" data-width="425" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1054" class="ax_default box_1">
          <div id="u1054_div" class=""></div>
          <div id="u1054_text" class="text ">
            <p><span>受托支付额度(元)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1055" class="ax_default box_1">
          <div id="u1055_div" class=""></div>
          <div id="u1055_text" class="text ">
            <p><span>100.00</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1056" class="ax_default" data-left="766" data-top="4100" data-width="362" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1057" class="ax_default box_1">
          <div id="u1057_div" class=""></div>
          <div id="u1057_text" class="text ">
            <p><span>受托支付是否行内标识</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1058" class="ax_default box_1">
          <div id="u1058_div" class=""></div>
          <div id="u1058_text" class="text ">
            <p><span>是</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1059" class="ax_default" data-left="834" data-top="4137" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1060" class="ax_default box_1">
          <div id="u1060_div" class=""></div>
          <div id="u1060_text" class="text ">
            <p><span>结束时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1061" class="ax_default box_1">
          <div id="u1061_div" class=""></div>
          <div id="u1061_text" class="text ">
            <p><span>2023-01-05</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1062" class="ax_default" data-left="330" data-top="4137" data-width="319" data-height="25">

        <!-- Unnamed (Rectangle) -->
        <div id="u1063" class="ax_default box_1">
          <div id="u1063_div" class=""></div>
          <div id="u1063_text" class="text ">
            <p><span>开始时间</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1064" class="ax_default box_1">
          <div id="u1064_div" class=""></div>
          <div id="u1064_text" class="text ">
            <p><span>2023-01-05</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1065" class="ax_default" data-left="237" data-top="4176" data-width="269" data-height="80">

        <!-- 添加 (Group) -->
        <div id="u1066" class="ax_default" data-label="添加" title="未选择任何文件" data-left="426" data-top="4176" data-width="80" data-height="80">

          <!-- Unnamed (Rectangle) -->
          <div id="u1067" class="ax_default box_1">
            <img id="u1067_img" class="img " src="images/授信订单详情/regen/u125.svg">
            <div id="u1067_text" class="text ">
              <p><span>图片</span></p>
            </div>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1068" class="ax_default label">
          <div id="u1068_div" class=""></div>
          <div id="u1068_text" class="text ">
            <p><span>受托支付证明材料</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1069" class="ax_default" data-left="1759" data-top="2609" data-width="111" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1070" class="ax_default label">
          <div id="u1070_div" class=""></div>
          <div id="u1070_text" class="text ">
            <p><span>客户简称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1071" class="ax_default label">
          <div id="u1071_div" class=""></div>
          <div id="u1071_text" class="text ">
            <p><span>XXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1072" class="ax_default" data-left="2283" data-top="2609" data-width="120" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1073" class="ax_default label">
          <div id="u1073_div" class=""></div>
          <div id="u1073_text" class="text ">
            <p><span>国别代码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1074" class="ax_default label">
          <div id="u1074_div" class=""></div>
          <div id="u1074_text" class="text ">
            <p><span>XXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1075" class="ax_default" data-left="1759" data-top="2647" data-width="120" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1076" class="ax_default label">
          <div id="u1076_div" class=""></div>
          <div id="u1076_text" class="text ">
            <p><span>客户评级</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1077" class="ax_default label">
          <div id="u1077_div" class=""></div>
          <div id="u1077_text" class="text ">
            <p><span>XXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1078" class="ax_default" data-left="2246" data-top="2647" data-width="148" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1079" class="ax_default label">
          <div id="u1079_div" class=""></div>
          <div id="u1079_text" class="text ">
            <p><span>客户名称(英文)</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1080" class="ax_default label">
          <div id="u1080_div" class=""></div>
          <div id="u1080_text" class="text ">
            <p><span>XXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1081" class="ax_default" data-left="1745" data-top="2683" data-width="125" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1082" class="ax_default label">
          <div id="u1082_div" class=""></div>
          <div id="u1082_text" class="text ">
            <p><span>有无中征码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1083" class="ax_default label">
          <div id="u1083_div" class=""></div>
          <div id="u1083_text" class="text ">
            <p><span>XXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1084" class="ax_default" data-left="2301" data-top="2683" data-width="97" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1085" class="ax_default label">
          <div id="u1085_div" class=""></div>
          <div id="u1085_text" class="text ">
            <p><span>中征码</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1086" class="ax_default label">
          <div id="u1086_div" class=""></div>
          <div id="u1086_text" class="text ">
            <p><span>XXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1087" class="ax_default" data-left="1887" data-top="343" data-width="94" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1088" class="ax_default label">
          <div id="u1088_div" class=""></div>
          <div id="u1088_text" class="text ">
            <p><span>最高学历</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1089" class="ax_default label">
          <div id="u1089_div" class=""></div>
          <div id="u1089_text" class="text ">
            <p><span>本科</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1090" class="ax_default label">
        <div id="u1090_div" class=""></div>
        <div id="u1090_text" class="text ">
          <p><span>学历信息</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1091" class="ax_default" data-left="1887" data-top="412" data-width="94" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1092" class="ax_default label">
          <div id="u1092_div" class=""></div>
          <div id="u1092_text" class="text ">
            <p><span>婚姻</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1093" class="ax_default label">
          <div id="u1093_div" class=""></div>
          <div id="u1093_text" class="text ">
            <p><span>已婚</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1094" class="ax_default label">
        <div id="u1094_div" class=""></div>
        <div id="u1094_text" class="text ">
          <p><span>婚姻信息</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1095" class="ax_default" data-left="1887" data-top="493" data-width="120" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1096" class="ax_default label">
          <div id="u1096_div" class=""></div>
          <div id="u1096_text" class="text ">
            <p><span>职业</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1097" class="ax_default label">
          <div id="u1097_div" class=""></div>
          <div id="u1097_text" class="text ">
            <p><span>XXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1098" class="ax_default label">
        <div id="u1098_div" class=""></div>
        <div id="u1098_text" class="text ">
          <p><span>工作信息</span></p>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1099" class="ax_default" data-left="2406" data-top="493" data-width="152" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1100" class="ax_default label">
          <div id="u1100_div" class=""></div>
          <div id="u1100_text" class="text ">
            <p><span>单位名称</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1101" class="ax_default label">
          <div id="u1101_div" class=""></div>
          <div id="u1101_text" class="text ">
            <p><span>XXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Group) -->
      <div id="u1102" class="ax_default" data-left="1845" data-top="578" data-width="162" data-height="20">

        <!-- Unnamed (Rectangle) -->
        <div id="u1103" class="ax_default label">
          <div id="u1103_div" class=""></div>
          <div id="u1103_text" class="text ">
            <p><span>家庭年收入</span></p>
          </div>
        </div>

        <!-- Unnamed (Rectangle) -->
        <div id="u1104" class="ax_default label">
          <div id="u1104_div" class=""></div>
          <div id="u1104_text" class="text ">
            <p><span>XXXXXX</span></p>
          </div>
        </div>
      </div>

      <!-- Unnamed (Rectangle) -->
      <div id="u1105" class="ax_default label">
        <div id="u1105_div" class=""></div>
        <div id="u1105_text" class="text ">
          <p><span>收入信息</span></p>
        </div>
      </div>

      <!-- Unnamed (Ellipse) -->
      <div id="u1106" class="ax_default ellipse">
        <img id="u1106_img" class="img " src="images/授信订单详情/regen/u996.svg">
        <div id="u1106_text" class="text ">
          <p><span>？</span></p>
        </div>
      </div>

      <!-- Unnamed (Speech Bubble) -->
      <div id="u1107" class="ax_default _形状">
        <img id="u1107_img" class="img " src="images/授信订单详情/regen/u997.svg">
        <div id="u1107_text" class="text ">
          <p><span style="font-family:'ArialMT', 'Arial', sans-serif;">{</span><span style="font-family:'PingFangSC-Regular', 'PingFang SC', sans-serif;">拒绝原因</span><span style="font-family:'ArialMT', 'Arial', sans-serif;">}</span></p>
        </div>
      </div>
    </div>
    <script src="resources/scripts/axure/ios.js"></script>


<div id="axureEventReceiverDiv" style="display:none"></div><div id="axureEventSenderDiv" style="display:none"></div></body></html>
'''

span_contents = extract_span_contents(html)
for content in span_contents:
    print(content.encode('utf-8'))
