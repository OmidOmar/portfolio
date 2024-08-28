// Function to generate a unique ID with random digits and alphabets
function generateUniqueId() {
  const digits = "0123456789";
  const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  let uniqueId = "";

  // Add 4 random digits
  for (let i = 0; i < 4; i++) {
    uniqueId += digits.charAt(Math.floor(Math.random() * digits.length));
  }

  // Add 4 random alphabets
  for (let i = 0; i < 4; i++) {
    uniqueId += letters.charAt(Math.floor(Math.random() * letters.length));
  }

  return uniqueId;
}

// Function to save the message as a JSON file
function saveMessage() {
  const name = document.getElementById("name").value;
  const email = document.getElementById("email").value;
  const subject = document.getElementById("subject").value;
  const message = document.getElementById("message").value;

  // Generate a unique message ID
  const messageId = generateUniqueId();

  // Create the message object
  const messageData = {
    id: messageId,
    name: name,
    email: email,
    subject: subject,
    message: message,
  };

  // Convert the message object to JSON
  const messageJson = JSON.stringify(messageData, null, 2);

  // Create a blob and save the data as a file
  const blob = new Blob([messageJson], { type: "application/json" });

  // Create a temporary link element to trigger download
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = `message_${messageId}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);

  // Clear the form after saving the message
  //document.getElementById("contactForm").reset();
}
