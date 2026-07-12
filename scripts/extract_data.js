const fs = require('fs');

function extractBalanced(text, startPos) {
  let i = startPos;
  while (i < text.length && text[i] === ' ') i++;
  if (text[i] !== '[') throw new Error('Expected [ at position ' + i);
  let depth = 0, inStr = false, quote = null, result = '';
  while (i < text.length) {
    const ch = text[i];
    if (inStr) {
      result += ch;
      if (ch === '\\') { i++; result += text[i]; }
      else if (ch === quote) { inStr = false; quote = null; }
    } else {
      if (ch === '"' || ch === "'" || ch === '`') { inStr = true; quote = ch; }
      else if (ch === '[' || ch === '{') { depth++; }
      else if (ch === ']' || ch === '}') { depth--; if (depth === 0) return result + ch; }
      result += ch;
    }
    i++;
  }
  throw new Error('Unbalanced brackets');
}

const html = fs.readFileSync('index.html', 'utf-8');
const scriptMatch = html.match(/<script>([\s\S]*?)<\/script>/);
if (!scriptMatch) { console.error('Script tag not found'); process.exit(1); }

const js = scriptMatch[1];
const p1 = extractBalanced(js, js.indexOf('const PART1 = ') + 'const PART1 = '.length);
const p2 = extractBalanced(js, js.indexOf('const PART2 = ') + 'const PART2 = '.length);

const part1 = eval(p1);
const part2 = eval(p2);

fs.writeFileSync('course/data.json', JSON.stringify({ part1: part1, part2: part2 }, null, 2));
console.log('OK: ' + part1.length + ' + ' + part2.length + ' = ' + (part1.length + part2.length) + ' lessons');
