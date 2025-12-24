export default function LightSwitch() {
  function handleClick() {
    let bodyStyle = document.body.style;
    if (bodyStyle.backgroundColor === 'black') {
      bodyStyle.backgroundColor = 'white';
    } else {
      bodyStyle.backgroundColor = 'black';
    }
  }

//fixed the code the error was this line <button onClick={handleClick()}> to <button onClick={handleClick}>
  return (
    <button onClick={handleClick}> 
      Toggle the lights
    </button>
  );
}
