const fs = require('fs');
const path = 'C:\\Users\\renu5\\Downloads\\mg-styles-15\\demos\\how-to-win-friends\\index.html';
let content = fs.readFileSync(path, 'utf8');

content = content.replace("zh:'电池',en:'BATTERY'", "zh:'SAMAJHNA',en:'NO MANIPULATION'");
content = content.replace("zh:'主板',en:'MAINBOARD'", "zh:'BINA ARGUMENT',en:'NO ARGUMENTS'");
content = content.replace("zh:'芯片',en:'CHIP'", "zh:'INSPIRE',en:'CRITICISM'");
content = content.replace("zh:'磁铁',en:'SPEAKER MAGNET'", "zh:'FEEL IMPORTANT',en:'MAKE THEM FEEL'");
content = content.replace("zh:'屏幕',en:'DISPLAY'", "zh:'COMPLETE SHIFT',en:'SIMPLE CHANGES'");
content = content.replace("02 对照元素周期表", "02 DEEPER SCIENCE");
content = content.replace("PERIODIC TABLE", "PSYCHOLOGY");
content = content.replace("种元素，出现在一部手机里", "Principles of Human Relations");
content = content.replace("03 按类别统计", "03 CORE CONCEPTS");
content = content.replace("BY CATEGORY · 共 70 种", "BY IMPACT");
content = content.replace("过渡金属", "Empathy");
content = content.replace("TRANSITION METALS", "UNDERSTANDING");
content = content.replace("稀土元素", "Influence");
content = content.replace("RARE EARTHS", "LEADERSHIP");

fs.writeFileSync(path, content, 'utf8');
console.log('Replaced more text successfully.');
