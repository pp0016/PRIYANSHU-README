const Database = require('C:/Users/renu5/AppData/Roaming/9router/runtime/node_modules/better-sqlite3');
const db = new Database('C:/Users/renu5/AppData/Roaming/9router/db/data.sqlite', { readonly: true });
const tables = db.prepare("SELECT name FROM sqlite_master WHERE type='table'").all();
console.log("Tables:", JSON.stringify(tables));
for (const t of tables) {
  if (t.name.toLowerCase().includes('key') || t.name.toLowerCase().includes('api') || t.name.toLowerCase().includes('setting') || t.name.toLowerCase().includes('config')) {
    try {
      const rows = db.prepare(`SELECT * FROM "${t.name}" LIMIT 5`).all();
      console.log(`\n--- ${t.name} ---`);
      console.log(JSON.stringify(rows, null, 2));
    } catch(e) { console.log(`Error reading ${t.name}: ${e.message}`); }
  }
}
db.close();
