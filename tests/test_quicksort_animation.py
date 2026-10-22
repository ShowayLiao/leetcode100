import pathlib
import re
import shutil
import subprocess
import unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
PAGE = ROOT / 'docs/animations/quicksort.html'

class QuickSortAnimationTests(unittest.TestCase):
    def test_trace_and_partition_invariants(self):
        self.assertTrue(PAGE.is_file(), 'animation page must exist')
        if not shutil.which('node'):
            self.skipTest('Node.js is required to validate the embedded animation engine')
        text = PAGE.read_text(encoding='utf-8-sig')
        engine = re.search(r'<script id="engine">(.*?)</script>', text, re.S)
        self.assertIsNotNone(engine)
        check = r'''
const assert = require('node:assert/strict');
let seed=23;
const rand=()=> (seed=(seed*1664525+1013904223)>>>0);
const cases=[[],[1],[3,1,2],[5,2,9,1,5,6],Array(24).fill(7),Array.from({length:24},(_,i)=>i),Array.from({length:24},(_,i)=>24-i),[-999999,0,999999]];
for(let t=0;t<200;t++) cases.push(Array.from({length:rand()%25},()=>rand()%21-10));
for(const input of cases){
 const before=input.slice(); const trace=buildTrace(input);
 assert.deepEqual(input,before,'must not modify caller input');
 assert.deepEqual(trace.at(-1).items.map(x=>x.value),before.slice().sort((a,b)=>a-b));
 for(let j=0;j<trace.length;j++){
  const s=trace[j];
  assert.equal(new Set(s.items.map(x=>x.id)).size,input.length);
  assert.deepEqual(s.items.map(x=>x.value).sort((a,b)=>a-b),before.slice().sort((a,b)=>a-b));
  if(s.valid && s.pivot!==null){
   for(let i=s.left;i<s.less;i++) assert.ok(s.items[i].value<s.pivot);
   for(let i=s.less;i<s.current;i++) assert.equal(s.items[i].value,s.pivot);
   for(let i=s.greater+1;i<=s.right;i++) assert.ok(s.items[i].value>s.pivot);
  }
  if(s.kind==='advance-right') assert.equal(s.current,trace[j-1].current,'right swap must be rechecked');
  assert.ok(s.stack.length<=Math.ceil(Math.log2(input.length+1))+1);
 }
}
assert.deepEqual(parseArray('3, -2，1 0'),[3,-2,1,0]);
for(const bad of ['','1 x','1.5','Infinity','1e3',Array(25).fill(1).join(' ')]) assert.throws(()=>parseArray(bad));
console.log('208 arrays: result, multiset, partition, stack, pointer and input checks passed');
'''
        result = subprocess.run(['node', '-'], input=engine.group(1)+'\n'+check, text=True, capture_output=True, encoding='utf-8', cwd=ROOT)
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)

if __name__ == '__main__':
    unittest.main()
