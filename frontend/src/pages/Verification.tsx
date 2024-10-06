import axios from "axios";
import { QRCodeSVG } from "qrcode.react";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Verification() {
  const GENERATE_URL = "https://rh.drismir.ca/api/generate_qr/14372197463";
  const CHECK_URL = "https://rh.drismir.ca/api/phone_scan/14372197463";
  const QR_SCANNED = "https://rh.drismir.ca/api/qr_scanned/14372197463";
  const [qr, setQr] = useState<string>("");
  const navigate = useNavigate();

  async function getUrl() {
    const response = await axios.get(GENERATE_URL); 

    setQr(response.data)

  }

  getUrl()

  async function checkVerified() {
    let response = null;
    try {
      response = await axios.get(QR_SCANNED)
      console.log(response.data)
    } catch (error) {
    }
    const response_text = await response?.data;
    console.log(response)

    if (response_text === "The QR code has been scanned") {
      navigate("/auth")
    }
  }

  useEffect(() => {
    const fetchData = async () => {
      await getUrl();
    };
    fetchData();
  }, []);


  useEffect(() => {
    const interval = setInterval(async () => {
      await checkVerified();
    }, 1000)
    return () => clearInterval(interval)
  }, [])

  useEffect(() => {
    const timeout = setTimeout(() => {
     // navigate('/auth');
    }, 8000)
    return () => clearTimeout(timeout);
  })


  return (
    <div className="h-[700px] bg-white mx-64 mt-10 rounded-xl flex items-center align-middle justify-center">
      <div className="flex flex-col items-center justify-center align-middle h-[100vh]">

        <QRCodeSVG value={qr} size={512} />
        <p className="text-black text-4xl">Scan me!</p>
      </div>
    </div>
  );
}
