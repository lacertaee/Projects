document.addEventListener('DOMContentLoaded', function() {

  // Send email
  document.querySelector('#compose-form').addEventListener('submit', send_mail);

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', compose_email);

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email() {
  document.querySelector('#see').innerHTML = '';

  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';

  // Clear out composition fields
  document.querySelector('#compose-recipients').value = '';
  document.querySelector('#compose-subject').value = '';
  document.querySelector('#compose-body').value = '';
}

function load_mailbox(mailbox) {
  document.querySelector('#see').innerHTML = '';

  // Show the mailbox and hide other views
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';

  // Show the mailbox name
  document.querySelector('#emails-view').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;
  
  fetch(`/emails/${mailbox}`)
  .then(response => response.json())
  .then(emails => {
    // Print emails
    console.log(emails);
    emails.forEach(email => {
      const parent = document.createElement('div');
      const parent2 = document.createElement('div');
      const view = document.createElement('div');
      const subj = document.createElement('div');
      const time = document.createElement('div');
      time.style.color = 'grey';
      view.style.fontWeight = 'bold';
      subj.style.paddingLeft = '10px';
      subj.innerHTML = `${email.subject}`;
      time.innerHTML = `${email.timestamp}`;
      view.innerHTML = `${email.sender}`;
      parent2.append(view, subj);
      parent2.style.display = 'flex';
      parent.style.border = '2px solid black';
      parent.style.padding = '4px';
      if (email.read === true){
        parent.style.background = 'Gainsboro';
      }
      parent.append(parent2, time);
      parent.style.display = 'flex';
      parent.style.justifyContent = 'space-between';
      parent.style.fontFamily = 'sans-serif';

      document.querySelector('#emails-view').append(parent);

      parent.addEventListener('click', () => {
        console.log('This element has been clicked!')
        document.querySelector('#emails-view').innerHTML = '';
        viewEmail(email.id, mailbox); 
      });
    });
  });
  view.innerHTML = '';
}

function send_mail(event){
  event.preventDefault();
  const recipients = document.querySelector('#compose-recipients').value;
  const body = document.querySelector('#compose-body').value;
  const subject = document.querySelector('#compose-subject').value;
  fetch('/emails', {
    method: 'POST',
    body: JSON.stringify({
      recipients: recipients,
      subject: subject,
      body: body
    })
  })
  .then(response => response.json())
  .then(result => {
    console.log(result);
    load_mailbox('sent');
  })
}

function viewEmail(id, type){
  fetch(`/emails/${id}`)
  .then(response => response.json())
  .then(email => {

    // Mark as read

    fetch(`/emails/${id}`, {
      method: 'PUT',
      body: JSON.stringify({
          read: true
      })
    })

    // Show email

    const show = document.createElement('div');
    show.innerHTML = `
      <h6>From: <nobr style="font-weight: normal;">${email.sender}</nobr></h6>
      <h6>To: <nobr style="font-weight: normal;">${email.recipients}</nobr></h6>
      <h6>Subject: <nobr style="font-weight: normal;">${email.subject}</nobr></h6>
      <h6>Timestamp: <nobr style="font-weight: normal;">${email.timestamp}</nobr></h6>
      <hr>
      <div>${email.body}</div>
      <hr>
    `;
    document.querySelector('#see').append(show);
    // Archieve
    if (type === 'inbox' || type === 'archive'){
      const arch = document.createElement('button');
      if (type === 'inbox'){
        arch.innerHTML = 'Archive';
      }else{
        arch.innerHTML = "Unarchive";
      }
      arch.className = 'btn btn-sm btn-outline-primary';
      document.querySelector('#see').append(arch);
      arch.addEventListener('click', () => {
        if (type === 'inbox'){
          fetch(`/emails/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                archived: true
            })
          })
          load_mailbox('archive');
        }else{
          fetch(`/emails/${id}`, {
            method: 'PUT',
            body: JSON.stringify({
                archived: false
            })
          })
          load_mailbox('inbox');
        }
      })
      const b = document.createElement('button');
      b.innerHTML = 'Reply';
      b.style.marginLeft = '10px';
      b.className = 'btn btn-sm btn-outline-primary';
      document.querySelector('#see').append(b);
      b.addEventListener('click', () => {
        compose_email();
        fetch(`/emails/${id}`)
        .then(response => response.json())
        .then(email => {
          document.querySelector('#compose-recipients').value = `${email.sender}`;
          document.querySelector('#compose-subject').placeholder = `Re: ${email.subject}`;
          document.querySelector('#compose-body').placeholder = `On ${email.timestamp} ${email.sender} wrote: ${email.body}`;
        });
      });  
    }
  });
}


