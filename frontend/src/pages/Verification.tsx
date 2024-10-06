import axios from "axios";
import { QRCodeSVG } from "qrcode.react";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Verification() {
  const URL = "https://rh.drismir.ca/api/phone_scan/14372197463";
  const [qr, setQr] = useState<string>("");
  const navigate = useNavigate();

  async function getUrl() {
    const response = await fetch(URL, {
      method: "GET",
      headers: {
        "Content-type": "application/json",
      },
    })

    if (!response.ok) {
      return "";
    }

    const response_text = await response.text()
    return response_text;
  }

  async function checkVerified() {
    let response = null;
    try {
    response = await axios.get("https://rh.drismir.ca/api/phone_scan/14372197463")
    } catch(error) {
    }
    const response_text = await response?.data;

    if (response_text === "asdf") {
      navigate("/auth")
    }
  }

  useEffect(() => {
    const fetchData = async () => {
     // const url = await getUrl();
      //setQr(url);
      setQr("rh.drismir.ca/api/phone_scan/"); // TODO: remove later
    };
    fetchData();
  }, []);


  useEffect(() => {
    const interval = setInterval( async () => {
      await checkVerified();
    }, 1000)
    return () => clearInterval(interval)
  }, [])

  useEffect(() => {
    const timeout = setTimeout(() => {
      navigate('/auth');
    }, 4000)
    return () => clearTimeout(timeout);
  })


  return (
    <div className="flex flex-col items-center justify-center align-middle h-[100vh]">

      <QRCodeSVG value={qr} size={256} />
      <p>Scan me!</p>
    </div>
  );
}
