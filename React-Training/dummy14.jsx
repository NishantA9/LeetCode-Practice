//Responding to Event Handlers in React

export default function App() {
  return (
    <Toolbar
      onPlayMovie={() => alert('Playing!')}
      onUploadImage={() => alert('Uploading!')}
      onSub={() => alert('Subscribed to FireEmperor!')}
    />
  );
}

function Toolbar({ onPlayMovie, onUploadImage, onSub }) {
  return (
    <div>
      <Button onClick={onPlayMovie}>
        Play Movie
      </Button>
      <Button onClick={onUploadImage}>
        Upload Image
      </Button>
      <Button onClick={onSub}>Subscribe</Button>
    </div>
  );
}

function Button({ onClick, children }) {
  return (
    <button onClick={onClick}>
      {children}
    </button>
  );
}
