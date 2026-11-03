// ปุ่มคัดลอกโค้ด
document.querySelectorAll('.code').forEach(box => {
  const btn = document.createElement('button');
  btn.className = 'copy'; btn.type = 'button'; btn.textContent = 'คัดลอก';
  btn.addEventListener('click', async () => {
    const text = box.querySelector('code').innerText;
    try { await navigator.clipboard.writeText(text); }
    catch (e) {
      const ta = document.createElement('textarea'); ta.value = text;
      document.body.appendChild(ta); ta.select(); document.execCommand('copy'); ta.remove();
    }
    btn.textContent = 'คัดลอกแล้ว'; btn.classList.add('ok');
    setTimeout(() => { btn.textContent = 'คัดลอก'; btn.classList.remove('ok'); }, 1500);
  });
  box.appendChild(btn);
});

// ติ๊กข้อที่ผ่าน (จำไว้ในเครื่องนี้)
const KEY = document.body.dataset.key || 'ds-lesson';
let saved = [];
try { saved = JSON.parse(localStorage.getItem(KEY) || '[]'); } catch (e) { saved = []; }
const tasks = [...document.querySelectorAll('.task[data-task]:not([data-task="bonus"])')];
function update() {
  const done = tasks.filter(t => t.querySelector('input').checked);
  tasks.forEach(t => t.classList.toggle('passed', t.querySelector('input').checked));
  document.getElementById('count').textContent = `ผ่าน ${done.length}/${tasks.length} ข้อ`;
  document.getElementById('meter').style.width = (done.length / tasks.length * 100) + '%';
  try { localStorage.setItem(KEY, JSON.stringify(done.map(t => t.dataset.task))); } catch (e) {}
}
tasks.forEach(t => {
  const cb = t.querySelector('input');
  cb.checked = saved.includes(t.dataset.task);
  cb.addEventListener('change', update);
});
update();
