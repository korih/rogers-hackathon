import { useState } from "react";
import { useNavigate } from "react-router-dom";
import axios from "axios";

export default function Login() {
  const SIM_SWAP_URL: string = "https://pplx.azurewebsites.net/api/rapid/v0/numberVerification/verify";
  const [phoneNumber, setPhoneNumber] = useState<string | null>('');
  const navigate = useNavigate();

  async function sendSimSwapRequest(): Promise<void> {
    const isVerified = await verifyPhoneNumber();
    if (!isVerified) {
      alert("Please Use a valid phone number")
      return;
    }
    navigate('/success')
    return Promise.resolve()
  }

  async function numberVerificationApi() {
    const header = {
      "Authorization": `Bearer bca7ba`,
      "Cache-Control": "no-cache",
      "accept": "application/json",
      "Content-Type": "application/json"
    }
    const body = { "phoneNumber": `${phoneNumber}` };

    const response = await axios.post(SIM_SWAP_URL, body, { headers: header })
    return response
  }


  async function verifyPhoneNumber() {
    if (phoneNumber === null || phoneNumber === '') {
      alert("Please Use a valid phone number")
      return false;
    }
    const verification_response = await numberVerificationApi();
    console.log(verification_response)
    verification_response.data

    if (verification_response.status !== 200 || verification_response.data.devicePhoneNumberVerified === false) {
      alert("Please Use Rogers Verified Phone Number")
      return false;
    }

    return phoneNumber.length === 11;
  }

  return (
    <main className="w-[100%] h-[100%] flex justify-center align-middle flex-col">

      <div className="h-[700px] bg-white m-64 rounded-xl">
        <section id="logo" className="flex justify-center align-middle mt-40 mb-40">
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
            className="w-[25vw] rounded-xl h-10" />
          <button
            className="w-[25vw] mt-2 mb-10 bg-gray"
            onClick={sendSimSwapRequest}>
            Login

          </button>
        </section>
      </div>

    </main>
  )
}
