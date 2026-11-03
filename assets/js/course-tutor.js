(() => {
  const button = document.getElementById('copy-tutor-prompt');
  const prompt = document.getElementById('tutor-start-prompt');
  const status = document.getElementById('tutor-copy-status');
  if (!button || !prompt || !status) return;
  button.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(prompt.value);
      status.textContent = 'Copied. Paste it into a new AI chat.';
    } catch (_) {
      prompt.focus();
      prompt.select();
      status.textContent = 'Select and copy the prompt above (Ctrl+C or ⌘C).';
    }
  });
  const revealReference = () => {
    const section = document.getElementById(location.hash.slice(1));
    if (section instanceof HTMLDetailsElement) section.open = true;
  };
  window.addEventListener('hashchange', revealReference);
  revealReference();
})();
