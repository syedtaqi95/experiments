import ReactAriaComponentsForm from "../components/ReactAriaComponentsForm";
import ReactSpectrumForm from "../components/ReactSpectrumForm";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center gap-8 py-24 font-sans">
      <h1 className="text-2xl font-bold">UI Library Comparison</h1>
      <div className="flex w-full max-w-5xl flex-row justify-evenly text-left">
        <div>
          <h1 className="text-lg font-bold">React Spectrum:</h1>
          <ReactSpectrumForm />
        </div>

        <div>
          <h1 className="text-lg font-bold">React Aria (Components API):</h1>
          <ReactAriaComponentsForm />
        </div>
      </div>
    </main>
  );
}
