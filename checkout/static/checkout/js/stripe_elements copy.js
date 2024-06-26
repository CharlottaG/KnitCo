const stripe = Stripe('pk_test_51PVTL2P3kNHn6Hc2EfhOYN5hml14PDsN6vsj2vinkgAXorTAvfl7yp7PsofJFk2Vurvni8PXCxxLQiKFRurVFyqZ00wX0MTg76');

const appearance = {
    theme: 'flat',
    variables: {
        colorPrimary: '#0570de',
        colorBackground: '#ffffff',
        colorText: '#30313d',
        colorDanger: '#df1b41',
        fontFamily: 'Ideal Sans, system-ui, sans-serif',
        spacingUnit: '2px',
        borderRadius: '4px',

      }
      rules: {
        '.Tab': {
          border: '1px solid #E0E6EB',
          boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02)',
        },
  
        '.Tab:hover': {
          color: 'var(--colorText)',
        },
  
        '.Tab--selected': {
          borderColor: '#E0E6EB',
          boxShadow: '0px 1px 1px rgba(0, 0, 0, 0.03), 0px 3px 6px rgba(18, 42, 66, 0.02), 0 0 0 2px var(--colorPrimary)',
        },
  
        '.Input--invalid': {
          boxShadow: '0 1px 1px 0 rgba(0, 0, 0, 0.07), 0 0 0 2px var(--colorDanger)',
        },
  
        // See all supported class names and selector syntax below
      }
    };

const options = {
  layout: {
    business: "KnitCo"
    type: 'accordion',
    defaultCollapsed: false,
    radios: false,
    spacedAccordionItems: true
  }
};
const clientSecret = {{CLIENT_SECRET}};
const elements = stripe.elements({ clientSecret, appearance });
const payment = elements.create('payment', options);
payment.mount('#payment-element');


// Handle realtime validation errors on the card element
payment.addEventListener('change', function (event) {
    var errorDiv = document.getElementById('payment-errors');
    if (event.error) {
        var html = `
            <span class="icon" role="alert">
                <i class="fas fa-times"></i>
            </span>
            <span>${event.error.message}</span>
        `;
        $(errorDiv).html(html);
    } else {
        errorDiv.textContent = '';
    }
});

