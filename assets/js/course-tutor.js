(() => {
  const button = document.getElementById('copy-tutor-prompt');
  const prompt = document.getElementById('tutor-start-prompt');
  const status = document.getElementById('tutor-copy-status');
  if (button && prompt && status) button.addEventListener('click', async () => {
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
    if (!section) return;
    for (let element = section; element; element = element.parentElement) {
      if (element instanceof HTMLDetailsElement) element.open = true;
    }
  };
  window.addEventListener('hashchange', revealReference);
  revealReference();
})();
  const codexButton = document.getElementById('copy-codex-setup-prompt');
  const codexPrompt = document.getElementById('codex-setup-prompt');
  const codexStatus = document.getElementById('codex-copy-status');
  if (codexButton && codexPrompt && codexStatus) codexButton.addEventListener('click', async () => {
    try {
      await navigator.clipboard.writeText(codexPrompt.value);
      codexStatus.textContent = 'Copied. Paste it into your AI agent.';
    } catch (_) {
      codexPrompt.focus();
      codexPrompt.select();
      codexStatus.textContent = 'Select and copy the prompt above (Ctrl+C or ⌘C).';
    }
  });
