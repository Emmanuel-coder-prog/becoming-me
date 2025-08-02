
function openModal(serviceName) {
  const modal = document.getElementById('customOrderModal');
  const serviceInput = document.getElementById('modalServiceInput');

  if (modal && serviceInput) {
    modal.classList.remove('hidden');
    serviceInput.value = serviceName;
  }
}

function closeModal() {
  const modal = document.getElementById('customOrderModal');
  if (modal) {
    modal.classList.add('hidden');
  }
}
