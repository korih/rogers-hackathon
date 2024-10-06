import { useState } from "react";

export default function Login() {
  const SIM_SWAP_URL: string = "https://pplx.azurewebsites.net/api/rapid/v0/simswap/check";
  const [phoneNumber, setPhoneNumber] = useState<string | null>('');

  async function sendSimSwapRequest(): Promise<void> {
    if (verifyPhoneNumber()) {
      console.log("phone number bad");
      return;
    }
    try {
      const response = await fetch(SIM_SWAP_URL, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ phoneNumber }),
      });

      const data = await response.json();
      console.log(data);
    } catch (error) {
      console.error(error);
    }
  }

  function verifyPhoneNumber(): boolean {
    if (phoneNumber === null || phoneNumber === '') {
      return false;
    }

    return phoneNumber.length === 11;
  }

  return (
    <main className="w-[100%] h-[100%] flex justify-center align-middle flex-col">
      <section id="logo" className="flex justify-center align-middle mb-40">
        <div className="flex">
          <img
            src="Logo.png"
            alt="logo"
            className="w-64 h-64" />
        </div>
      </section>

      <section id="login" className="flex flex-col items-center">
        <input
          type="text"
          name="phone-number"
          value={phoneNumber || ''}
          onChange={(e) => setPhoneNumber(e.target.value)}
          className="w-[25vw]" />
        <button
          className="w-[25vw]"
          onClick={sendSimSwapRequest}>
          Login

        </button>
      </section>

    </main>
  )
}
