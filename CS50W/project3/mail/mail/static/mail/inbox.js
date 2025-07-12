document.addEventListener('DOMContentLoaded', function() {

  // Use buttons to toggle between views
  document.querySelector('#inbox').addEventListener('click', () => load_mailbox('inbox'));
  document.querySelector('#sent').addEventListener('click', () => load_mailbox('sent'));
  document.querySelector('#archived').addEventListener('click', () => load_mailbox('archive'));
  document.querySelector('#compose').addEventListener('click', () => compose_email({}));

  // By default, load the inbox
  load_mailbox('inbox');
});

function compose_email( ) {
  
  // Show compose view and hide other views
  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'block';
  document.querySelector('#email-view').style.display = 'none';

  let composeTitle = document.querySelector('#compose-title')
  let composeRecipients = document.querySelector('#compose-recipients')
  let composeSubject = document.querySelector('#compose-subject')
  let composeBody = document.querySelector('#compose-body')
  let form = document.querySelector('#compose-form')




  if (!email.id ) {
    composeTitle.innerHTML = 'New Email'
    composeRecipients.value = '';
    composeSubject.value = '';
    composeBody.value = ''; 

  } else {
    composeTitle.innerHTML = 'Response'
    composeRecipients.value = email.sender;    

    email.subject.includes('Re:')
      ? composeSubject.value = email.subject
      : composeSubject.value = `Re: ${email.subject}`
      
      let reBody = `
      On ${email.timestamp} ${email.sender} wrote:
      ${email.body}
      _________________________
      
      `
      composeBody.value = reBody
    }
 
    
    form.addEventListener('submit', (e) => {
      e.preventDefault()
      e.stopImmediatePropagation()
      const data = {
          recipients: composeRecipients.value,
          subject: composeSubject.value,
          body: composeBody.value
      }      
      
      sendEmail(data)   
     })

}

function load_mailbox (mailbox) {
  // Show the mailbox and hide other views
  
  document.querySelector('#emails-view').style.display = 'block';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'none';
  // Show the mailbox name
  document.querySelector('#view-title').innerHTML = `<h3>${mailbox.charAt(0).toUpperCase() + mailbox.slice(1)}</h3>`;

  
  
  let tbody = document.querySelector('#tbody')
  tbody.innerHTML = ''

  fetch(`/emails/${mailbox}`,{
    method: 'GET'
  },
  )
    .then(response => response.json())
    .then(emails => { 
        
        emails.map((item) => {
          let from = document.createElement('td')
          let subject = document.createElement('td')
          let timestamp = document.createElement('td')
          let archiveTd = document.createElement('td')
          
          let button = document.createElement('button')       
          button.setAttribute('class', 'btn btn-outline-primary btn-sm rounded-pill')
          button.setAttribute('id', `${item.id}`)
          if (item.archived == true) {
            button.innerHTML = 'Desarchive'
            
          } else {
            button.innerHTML = 'Archive'
          }
          button.addEventListener('click', () => archived(item.id, item.archived))

          from.innerHTML = item.sender
          subject.innerHTML = item.subject
          timestamp.innerHTML = item.timestamp
          archiveTd.appendChild(button)

          from.addEventListener('click', () => email(item.id))
          subject.addEventListener('click', () => email(item.id))
          timestamp.addEventListener('click', () => email(item.id))

          let row = document.createElement('tr')

          if (item.read == true && mailbox!= 'sent') {
            row.classList.add('table-active')
          }

          row.appendChild(from)
          row.appendChild(subject)
          row.appendChild(timestamp)

          if (mailbox != 'sent') {
            row.appendChild(archiveTd)            
          }

          row.setAttribute('id', `${item.id}`)

          

          tbody.appendChild(row)

          })
        }
      
    )
    .catch(error => console.error('Error:', error))
}

const email = (emailId) => {
  
  console.log(emailId)

  document.querySelector('#emails-view').style.display = 'none';
  document.querySelector('#compose-view').style.display = 'none';
  document.querySelector('#email-view').style.display = 'block';
  let btnReply = document.querySelector('#reply-btn')
  let message = document.querySelector('#body-text')
  message.innerHTML = ''
  let user = document.querySelector('#user').innerHTML
  
  fetch(`/emails/${emailId}`, {
    method: 'GET'
  }
  )
    .then(response => response.json())
    .then(email => {     
      

      email.sender === user
        ? btnReply.style.display = 'none'
        : btnReply.style.display = 'block'
        

      btnReply.addEventListener('click', () => {compose_email(email)})
      document.querySelector('#subject').innerHTML = email.subject
      document.querySelector('#from').innerHTML = email.sender
      document.querySelector('#to').innerHTML = email.recipients      
      document.querySelector('#timestamp').innerHTML = email.timestamp

      email.body.split(/(?:\r?\n)+/).map(item => {
        let paragraph = document.createElement('p')
        paragraph.innerHTML = item
        message.appendChild(paragraph)
      })

    }).catch(error => console.error('Error:', error))
  
  fetch(`/emails/${emailId}`, {
    method: 'PUT',    
    headers: {
    'Content-Type': 'application/json'
  },
    body: JSON.stringify({
      read: true
    })
  })
    .catch(error => console.error('Error:', error))

}

const archived = (emailId, archived) => {

  const isArchived = () => {
    if (archived) {
      return false
    } else {
      return true
    }
  }

  fetch(`/emails/${emailId}`, {
    method: 'PUT',
    headers: {
    'Content-Type': 'application/json'
  },
    body: JSON.stringify({
    archived: isArchived()
      })
  }).then(response => {    
    if (response.ok) {
    load_mailbox('inbox')
  }})    
  .catch(error => console.error('Error:', error))
    
}

sendEmail = (data) => {
  
  fetch('/emails', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(data)
        
    })
    .then(response => response.json())
    .then(result => {
    // Print result
    console.log(result);
    })
    .catch(error => console.error('Error:', error))
    .finally(()=>load_mailbox('sent'))
}


