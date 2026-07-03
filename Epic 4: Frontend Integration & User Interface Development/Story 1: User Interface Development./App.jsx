import "./App.css";

function App() {
  return (
    <div className="container">
      <div className="left">
        <h1>
          Take Control of Your <span>Financial Future</span>
        </h1>

        <p>
          AI-powered debt management that helps you negotiate smarter,
          settle faster, and live debt-free.
        </p>

        <div className="cards">
          <div className="card">
            <h2>40-75%</h2>
            <p>Settlement Range</p>
          </div>

          <div className="card">
            <h2>AI</h2>
            <p>Powered Strategy</p>
          </div>

          <div className="card">
            <h2>Free</h2>
            <p>To Get Started</p>
          </div>
        </div>
      </div>

      <div className="right">
        <div className="login-box">

          <h2>Welcome Back</h2>

          <p>Sign in to your dashboard</p>

          <input
            type="email"
            placeholder="Email Address"
          />

          <input
            type="password"
            placeholder="Password"
          />

          <button>Sign In</button>
        </div>
      </div>
    </div>
  );
}

export default App;
