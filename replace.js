const fs = require('fs');
const path = 'C:\\Users\\renu5\\Downloads\\mg-styles-15\\demos\\how-to-win-friends\\index.html';
let content = fs.readFileSync(path, 'utf8');

content = content.replace('一部手机里，', 'KABHI NOTICE KIYA?');
content = content.replace('藏着多少种元素？', 'TRUST & RESPECT.');
content = content.replace('HOW MANY ELEMENTS HIDE INSIDE ONE PHONE?', 'HOW TO WIN FRIENDS & INFLUENCE PEOPLE');
content = content.replace('拆开一部智能手机，逐一对照元素周期表', 'SAHI BAAT. Phir bhi... REJECTED!');

fs.writeFileSync(path, content, 'utf8');
console.log('Replaced successfully.');
