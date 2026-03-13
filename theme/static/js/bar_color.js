function getGradientColor(pct) {
  const gradient = [
    { pct: 0, color: [25, 58, 183] },   
    { pct: 50, color: [106, 114, 130] },   
    { pct: 100, color: [91, 0, 5] }
  ];

  let lower = gradient[0];
  let upper = gradient[gradient.length - 1];

  for (let i = 1; i < gradient.length; i++) {
    if (pct <= gradient[i].pct) {
      upper = gradient[i];
      lower = gradient[i - 1];
      break;
    }
  }

  const rangePct = (pct - lower.pct) / (upper.pct - lower.pct);

  const r = Math.round(lower.color[0] + rangePct * (upper.color[0] - lower.color[0]));
  const g = Math.round(lower.color[1] + rangePct * (upper.color[1] - lower.color[1]));
  const b = Math.round(lower.color[2] + rangePct * (upper.color[2] - lower.color[2]));

  return `rgb(${r}, ${g}, ${b})`;
}

document.querySelectorAll(".gradient-progress").forEach(bar => {

  const value = parseFloat(bar.dataset.value);
  const min = parseFloat(bar.dataset.min);
  const max = parseFloat(bar.dataset.max);
  console.log(value, min, max)

  const percent = ((value - min) / (max - min)) * 100;

  bar.value = percent;

  const color = getGradientColor(percent);

  bar.style.setProperty("color", color);
  bar.value = percent;
  // bar.min = min;
  bar.max = 100;
});