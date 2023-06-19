function initTask(subTask) {
 subTask.gridInfos = {
     languageStrings: {
          sl: {}
     },
     hideControls: {
          restart: false,
          saveOrLoad: false,
          loadBestAnswer: false,
          speedSlider: false,
          backToFirst: false,
          nextStep: false,
          goToEnd: false
     },
     hasGravity: false,
     introMaxHeight: "33%",
     maxListSize: 100,
     scrollbars: true,
     zoom: {
          controls: true,
          scale: 1
     },
     actionDelay: 400,
     blocklyColourTheme: "bwinf",
     maxInstructions: 0,
     includeBlocks: {
          groupByCategory: true,
          generatedBlocks: {
               robot: []
          },
          standardBlocks: {
               includeAll: false,
               wholeCategories: [],
               singleBlocks: [],
               excludedBlocks: []
          }
     },
     startingExample: {
          blockly: "<xml xmlns='http://www.w3.org/1999/xhtml'><block type='robot_start' id='?PYegoooe[j?}[Q@H/0J' deletable='false' movable='false' editable='false' x='0' y='0'><next><block type='controls_repeat_ext' id='SSu+)TuGuUx)z20xh1I='><value name='TIMES'><shadow type='math_number' id='OubPnKeYdH`n.lX}W2~*'><field name='NUM'>4</field></shadow></value><statement name='DO'><block type='moveSimple' id='FKwoqsV~[yfim;aHnQ2{'><field name='PARAM_0'>E</field></block></statement><next><block type='transport' id='+x+4|xM3)I68_t,a~m~g'><field name='PARAM_0'>pick</field><next><block type='controls_repeat_ext' id='k.]IRB=@:BRAtY{,AyE*'><value name='TIMES'><shadow type='math_number' id='6.`-1A66+nb)2h.`*uJ='><field name='NUM'>4</field></shadow></value><statement name='DO'><block type='moveSimple' id='/7?GyX@b}J?8C|uMR#hC'><field name='PARAM_0'>E</field></block></statement><next><block type='transport' id='#c*N[];XUa;64mV*o3T8'><field name='PARAM_0'>drop</field><next><block type='moveSimple' id='SJqSUui|h8)vzLhiD*pd'><field name='PARAM_0'>S</field><next><block type='controls_repeat_ext' id='hM+=5x.ZpkN*7amcO`5j'><value name='TIMES'><shadow type='math_number' id='pKToJONPC5}@*bTdY.b!'><field name='NUM'>5</field></shadow></value><statement name='DO'><block type='moveSimple' id='RkGLpPfK-P7#CUL/022G'><field name='PARAM_0'>W</field></block></statement><next><block type='transport' id='..rc0V0r6v;Iy]?i@cCu'><field name='PARAM_0'>pick</field><next><block type='controls_repeat_ext' id='03JzSJ*.c:m/LcDA9MYs'><value name='TIMES'><shadow type='math_number' id='}i0|sa(nEj1wF;77}pp|'><field name='NUM'>5</field></shadow></value><statement name='DO'><block type='moveSimple' id='}w:,;/o`dz=v-jd#~0;!'><field name='PARAM_0'>E</field></block></statement><next><block type='transport' id='qRS*rqJ#BcIFTz|ch*z#'><field name='PARAM_0'>drop</field><next><block type='moveSimple' id='xWe1/s.7z3+_*uWWwenq'><field name='PARAM_0'>S</field><next><block type='controls_repeat_ext' id='kLvC_,i1[Ll2[Wjmh_b='><value name='TIMES'><shadow type='math_number' id='5H/e*0U)qO-TfSl0O7F['><field name='NUM'>6</field></shadow></value><statement name='DO'><block type='moveSimple' id='Z18V0cc1:M2-;qhN[1ML'><field name='PARAM_0'>W</field></block></statement><next><block type='transport' id='7?ANWc:pm-e0[KCTS}4|'><field name='PARAM_0'>pick</field><next><block type='controls_repeat_ext' id='Da]uNs|!T6ohotb(u(/M'><value name='TIMES'><shadow type='math_number' id='Ay9krB=EGZ8FQ3xY@Nl|'><field name='NUM'>6</field></shadow></value><statement name='DO'><block type='moveSimple' id='.KEe7bOI,Dbur/odr7:_'><field name='PARAM_0'>E</field></block></statement><next><block type='transport' id='/4}gjY:V_WXg3|)t(q3h'><field name='PARAM_0'>drop</field></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block></next></block><additional>{}</additional></xml>"
     },
     checkEndEveryTurn: false,
     checkEndCondition: (context, lastTurn) => { 
	robotEndConditions.checkCombiner(context, lastTurn, [
		//,
		(context, lastTurn) => { robotEndConditions.checkItemCoincidence(context, lastTurn, {category: "transportable0"}, {category: "image1"}, [], {}, {}) }
	])
},
     ignoreInvalidMoves: false,
     border: 0.05,
     backgroundColour: "#000000",
     backgroundTile: "tiles/trava.png",
     borderColour: "#000000",
     showLabels: false,
     cellSide: 60,
     numberOfRobots: 1,
     itemTypes: {
          robot0: {
               img: "characters/bee_all_8_sides.png",
               zOrder: 20,
               value: 0,
               nbStates: 8,
               category: {
                    "robot": true
               }
          },
          image0: {
               num: 4,
               img: "objects/flower_without_dust.png",
               zOrder: 2,
               category: {
                    "image": true
               },
               value: 0
          },
          image1: {
               num: 5,
               img: "objects/honeycomb_empty.png",
               zOrder: 3,
               category: {
                    "image": true
               },
               value: 0
          },
          transportable0: {
               num: 6,
               img: "objects/flower_dust.png",
               zOrder: 4,
               category: {
                    "transportable": true
               },
               value: 0
          }
     }
};
subTask.data = {
     easy: [
          {
               tiles: [[1, 1, 1, 1, 4, 1, 1, 1, 5], 
 [1, 1, 1, 4, 1, 1, 1, 1, 5], 
 [1, 1, 4, 1, 1, 1, 1, 1, 5]],
               initItems: [
                    {
                         row: 0,
                         col: 0,
                         type: "robot0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 2,
                         col: 2,
                         type: "transportable0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 0,
                         col: 4,
                         type: "transportable0",
                         dir: 0,
                         value: 0
                    },
                    {
                         row: 1,
                         col: 3,
                         type: "transportable0",
                         dir: 0,
                         value: 0
                    }
               ]
          }
     ]
};
initBlocklySubTask(subTask); 
}