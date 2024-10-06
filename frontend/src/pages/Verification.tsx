import { QRCodeSVG } from "qrcode.react";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

export default function Verification() {
  const URL = "http://localhost:5000/api/phone_scan/";
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
    const response = await fetch(URL, {
      method: "GET",
      headers: {
        "Content-type": "application/json",
      },
    })

    const response_text = await response.text();

    if (response_text === "asdf") {
      navigate("/authentications")
    }
  }

  useEffect(() => {
    const fetchData = async () => {
      const url = await getUrl();
      setQr(url);
      setQr("www.gooogle.com"); // TODO: remove later
    };
    fetchData();
  }, []);


  useEffect(() => {
    const interval = setInterval( async () => {
      checkVerified();
    }, 1000)
    return () => clearInterval(interval)
  }, [])


  return (
    <div className="flex flex-col items-center justify-center align-middle h-[100vh]">

      <QRCodeSVG value={qr} size={256} />
      <p>Scan me!</p>
    </div>
  );
}
