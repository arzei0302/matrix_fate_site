import React, { useState } from "react";
import cals from "../../assets/shema.png";
import "./NumerologyChart.scss";



const NumerologyChart = ({ numbers = {},  }) => {
  return (
    <div className="numerlogyChart">
      <div className="shema">
        <img src={cals}  alt="Numerology Chart" />
        <div className="top1 circle large ">{numbers?.b ?? 0}</div>
        <div className="top2 circle medium ">{numbers.b1 ?? 0}</div>
        <div className="top3 circle small ">{numbers.b2 ?? 0}</div>
        <div className="top4 circle small ">{numbers.m ?? 0}</div>

        <div className="topRight1 circle large outlined">{numbers.g ?? 0}</div>
        <div className="topRight2 circle medium outlined">{numbers.g1 ?? 0}</div>
        <div className="topRight3 circle small outlined">{numbers.g2 ?? 0}</div>

        <div className="right1 circle large ">{numbers.c ?? 0}</div>
        <div className="right2 circle medium outlined">{numbers.c1 ?? 0}</div>
        <div className="right3 circle small ">{numbers.c2 ?? 0}</div>
        <div className="right4 circle mediumPlus outlined">{numbers.e2 ?? 0}</div>
        <div className="right5 circle medium outlined">{numbers.e1 ?? 0}</div>

        <div className="center circle large "> {numbers.e ?? 0} </div>

        <div className="bottomRight1 circle large outlined">{numbers.h ?? 0}</div>
        <div className="bottomRight2 circle medium outlined">{numbers.h1 ?? 0}</div>
        <div className="bottomRight3 circle small outlined">{numbers.h2 ?? 0}</div>
        <div className="bottomRight4 circle small outlined">{numbers.j ?? 0}</div>
        <div className="bottomRight5 circle small outlined">{numbers.k ?? 0}</div>
        <div className="bottomRight6 circle small outlined">{numbers.l ?? 0}</div>

        <div className="bottom1 circle large ">{numbers.d ?? 0}</div>
        <div className="bottom2 circle medium outlined">{numbers.d1 ?? 0}</div>
        <div className="bottom3 circle small ">{numbers.d2 ?? 0}</div>

        <div className="bottomLeft1 circle large outlined">{numbers.i ?? 0}</div>
        <div className="bottomLeft2 circle medium outlined">{numbers.i1 ?? 0}</div>
        <div className="bottomLeft3 circle small outlined">{numbers.i2 ?? 0}</div>

        <div className="left1 circle large ">{numbers.a ?? 0}</div>
        <div className="left2 circle medium ">{numbers.a1 ?? 0}</div>
        <div className="left3 circle small ">{numbers.a2 ?? 0}</div>
        <div className="left4 circle small  ">{numbers.n ?? 0}</div>

        <div className="topLeft1 circle large outlined">{numbers.f ?? 0}</div>
        <div className="topLeft2 circle medium outlined">{numbers.f1 ?? 0}</div>
        <div className="topLeft3 circle small outlined">{numbers.a2 ?? 0}</div>


        <div className="year21 number">{numbers.b21_22 ?? 0}</div>
        <div className="year22 number">{numbers.b22_23 ?? 0}</div>
        <div className="year23 number">{numbers.b23_24 ?? 0}</div>
        <div className="year24 number">{numbers.b25 ?? 0}</div>
        <div className="year25 number">{numbers.b26_27 ?? 0}</div>
        <div className="year26 number">{numbers.b27_28 ?? 0}</div>
        <div className="year27 number">{numbers.b28_29 ?? 0}</div>
        

        
        <div className="year31 number">{numbers.g31_32 ?? 0}</div>
        <div className="year32 number">{numbers.g32_33 ?? 0}</div>
        <div className="year33 number">{numbers.g33_34 ?? 0}</div>
        <div className="year34 number">{numbers.g35 ?? 0}</div>
        <div className="year35 number">{numbers.g36_37 ?? 0}</div>
        <div className="year36 number">{numbers.g37_38 ?? 0}</div>
        <div className="year37 number">{numbers.g38_39 ?? 0}</div>
        

        <div className="year41 number">{numbers.c41_42 ?? 0}</div>
        <div className="year42 number">{numbers.c42_43 ?? 0}</div>
        <div className="year43 number">{numbers.c43_44 ?? 0}</div>
        <div className="year44 number">{numbers.c45 ?? 0}</div>
        <div className="year45 number">{numbers.c46_47 ?? 0}</div>
        <div className="year46 number">{numbers.c47_48 ?? 0}</div>
        <div className="year47 number">{numbers.c48_49 ?? 0}</div>
   
        <div className="year51 number">{numbers.h51_52 ?? 0}</div>
        <div className="year52 number">{numbers.h52_53 ?? 0}</div>
        <div className="year53 number">{numbers.h53_54 ?? 0}</div>
        <div className="year54 number">{numbers.h55 ?? 0}</div>
        <div className="year55 number">{numbers.h56_57 ?? 0}</div>
        <div className="year56 number">{numbers.h57_58 ?? 0}</div>
        <div className="year57 number">{numbers.h58_59 ?? 0}</div>
   
   
        <div className="year61 number">{numbers.d61_62 ?? 0}</div>
        <div className="year62 number">{numbers.d62_63 ?? 0}</div>
        <div className="year63 number">{numbers.d63_64 ?? 0}</div>
        <div className="year64 number">{numbers.d65 ?? 0}</div>
        <div className="year65 number">{numbers.d66_67 ?? 0}</div>
        <div className="year66 number">{numbers.d67_68 ?? 0}</div>
        <div className="year67 number">{numbers.d68_69 ?? 0}</div>
   
     
        <div className="year71 number">{numbers.i71_72 ?? 0}</div>
        <div className="year72 number">{numbers.i72_73 ?? 0}</div>
        <div className="year73 number">{numbers.i73_74 ?? 0}</div>
        <div className="year74 number">{numbers.i75 ?? 0}</div>
        <div className="year75 number">{numbers.i76_77 ?? 0}</div>
        <div className="year76 number">{numbers.i77_78 ?? 0}</div>
        <div className="year77 number">{numbers.i78_79 ?? 0}</div>
  
        <div className="year1 number">{numbers.a1_2 ?? 0}</div>
        <div className="year2 number">{numbers.a2_3 ?? 0}</div>
        <div className="year3 number">{numbers.a3_4 ?? 0}</div>
        <div className="year4 number">{numbers.a5 ?? 0}</div>
        <div className="year5 number">{numbers.a6_7 ?? 0}</div>
        <div className="year6 number">{numbers.a7_8 ?? 0}</div>
        <div className="year7 number">{numbers.a8_9 ?? 0}</div>
   
        <div className="year11 number">{numbers.f11_12 ?? 0}</div>
        <div className="year12 number">{numbers.f12_13 ?? 0}</div>
        <div className="year13 number">{numbers.f13_14 ?? 0}</div>
        <div className="year14 number">{numbers.f15 ?? 0}</div>
        <div className="year15 number">{numbers.f16_17 ?? 0}</div>
        <div className="year16 number">{numbers.f17_18 ?? 0}</div>
        <div className="year17 number">{numbers.f18_19 ?? 0}</div>
  

      </div>
    </div>
  );
};

export default NumerologyChart;
