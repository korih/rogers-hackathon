import axios from "axios";
import { useState } from "react";

export default function AuthorizationFail() {

  const PHONE_NUMER_URL: string = "https://pplx.azurewebsites.net/api/rapid/v0/numberVerification/verify";
  const LOCATION_URL: string = "https://pplx.azurewebsites.net/api/rapid/v0/location-verification/verify";
  const SIM_SWAP_URL: string = "https://pplx.azurewebsites.net/api/rapid/v0/simswap/check";

  const [phone, setPhone] = useState(0)
  const [location, setLocation] = useState(0)
  const [sim, setSim] = useState(0)

  async function numberVerificationApi() {
    const header = {
      "Authorization": `Bearer bca7ba`,
      "Cache-Control": "no-cache",
      "accept": "application/json",
      "Content-Type": "application/json"
    }
    const body = { "phoneNumber": "14372197463" };

    const response = await axios.post(PHONE_NUMER_URL, body, { headers: header })

    if (response.status !== 200) {
      setPhone(2)
    } else {
      setPhone(1)
    }
    return response
  }

  async function LocationVerificationApi() {
    const header = {
      "Authorization": `Bearer bca7ba`,
      "Cache-Control": "no-cache",
      "accept": "application/json",
      "Content-Type": "application/json"
    }
    const body = {
      "device": {
        "phoneNumber": "14372197463"
      },
      "area": {
        "type": "Circle",
        "location": {
          "latitude": 49.261177,
          "longitude": 123.249161
        },
        "accuracy": 50
      }
    };

    const response = await axios.post(LOCATION_URL, body, { headers: header })
    if (response.data.verificationResult !== true) {
      setLocation(2)
    } else {
      setLocation(1)
    }
    return response
  }

  async function simSwapApi() {
    const header = {
      "Authorization": `Bearer bca7ba`,
      "Cache-Control": "no-cache",
      "accept": "application/json",
      "Content-Type": "application/json"
    }
    const body = { "phoneNumber": "14372197463" };

    const response = await axios.post(SIM_SWAP_URL, body, { headers: header })
    if (response.status !== 200) {
      setSim(2)
    } else {
      setSim(1)
    }
    return response
  }

  async function fetchAll() {
    await simSwapApi();
    await numberVerificationApi();
    await LocationVerificationApi();
  }

  fetchAll()


  return (
    <div className="h-[700px] bg-white mx-64 mt-10 rounded-xl flex items-center align-middle justify-center">
      <div className="flex flex-col items-center align-middle justify-center">
        <div className="flex mt-[100px] mb-[200px] align-middle justify-center items-center">
          <div className="mr-[50px]">
            <h1>Number Verification</h1>
          </div>
          <div className="w-64">
            {phone === 0 && <img src="Loading.svg" alt="Loading" className="w-[50px] h-[50px]" />}
            {phone === 1 && <img src="Good_check.png" alt="Success" className="w-[50px] h-[50px]" />}
            {phone === 2 && <img src="Bad_Check.jpg" alt="Error" className="w-[50px] h-[50px]" />}
          </div>
        </div>

        <div className="flex mb-[200px]">
          <div className="mr-[50px]">
            <h1>Location Verification</h1>
          </div>
          <div className="w-64">
            {location === 0 && <img src="Loading.svg" alt="Loading" className="w-[50px] h-[50px]" />}
            {location === 1 && <img src="Good_check.png" alt="Success" className="w-[50px] h-[50px]" />}
            {location === 2 && <img src="Bad_Check.jpg" alt="Error" className="w-[50px] h-[50px]" />}
          </div>
        </div>

        <div className="flex">
          <div className="mr-[50px]">
            <h1>Sim Verification</h1>
          </div>
          <div className="w-64">
            {sim === 0 && <img src="Loading.svg" alt="Loading" className="w-[50px] h-[50px]" />}
            {sim === 1 && <img src="Good_check.png" alt="Success" className="w-[50px] h-[50px]" />}
            {sim === 2 && <img src="Bad_Check.jpg" alt="Error" className="w-[50px] h-[50px]" />}
          </div>
        </div>
      </div>
    </div>
  );
}

