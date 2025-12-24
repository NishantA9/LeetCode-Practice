export default function ColorSwitch({
  onChangeColor
}) {
  return (
    <button >
      Change color
    </button>
  );
}

//change the above code to this below code to make it work

export default function ColorSwitch({
  onChangeColor
}) {
  return (
    <button onClick={e => {
      e.stopPropagation();
      onChangeColor();
    }}>
      Change color
    </button>
  );
}
