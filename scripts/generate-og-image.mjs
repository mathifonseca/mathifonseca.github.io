// Generates the social share (OpenGraph) card at public/assets/og-image.png
// Run with: node scripts/generate-og-image.mjs
import sharp from 'sharp';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const __dirname = dirname(fileURLToPath(import.meta.url));
const root = join(__dirname, '..');

const W = 1200;
const H = 630;
const PORTRAIT = 380; // diameter
const PORTRAIT_X = 760;
const PORTRAIT_Y = (H - PORTRAIT) / 2;

// Brand colors (from src/styles/global.css)
const accentLight = '#c561f6';
const accentRegular = '#7611a6';
const bgDark = '#090b11';

const bg = Buffer.from(`
<svg width="${W}" height="${H}" viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <radialGradient id="glow" cx="78%" cy="35%" r="70%">
      <stop offset="0%" stop-color="${accentRegular}" stop-opacity="0.55"/>
      <stop offset="55%" stop-color="${accentRegular}" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="${bgDark}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="title" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="#ffffff"/>
      <stop offset="100%" stop-color="${accentLight}"/>
    </linearGradient>
  </defs>

  <rect width="${W}" height="${H}" fill="${bgDark}"/>
  <rect width="${W}" height="${H}" fill="url(#glow)"/>

  <!-- accent rail -->
  <rect x="0" y="0" width="12" height="${H}" fill="${accentRegular}"/>

  <text x="80" y="248" font-family="Helvetica, Arial, sans-serif" font-size="78" font-weight="700" fill="url(#title)">Mathias Fonseca</text>
  <text x="82" y="316" font-family="Helvetica, Arial, sans-serif" font-size="40" font-weight="600" fill="${accentLight}">Principal Solutions Architect</text>

  <rect x="84" y="356" width="64" height="4" rx="2" fill="${accentRegular}"/>

  <text x="80" y="430" font-family="Helvetica, Arial, sans-serif" font-size="29" font-weight="400" fill="#c3c9d5">Payments · Fraud · Software · Teaching</text>
  <text x="80" y="474" font-family="Helvetica, Arial, sans-serif" font-size="29" font-weight="400" fill="#8a93a6">Berlin · 15+ years · 50+ PSP integrations</text>
</svg>`);

// Circular portrait
const circleMask = Buffer.from(
  `<svg width="${PORTRAIT}" height="${PORTRAIT}"><circle cx="${PORTRAIT / 2}" cy="${PORTRAIT / 2}" r="${PORTRAIT / 2}" fill="#fff"/></svg>`,
);

const portrait = await sharp(join(root, 'public/assets/portrait.png'))
  .resize(PORTRAIT, PORTRAIT, { fit: 'cover', position: 'top' })
  .composite([{ input: circleMask, blend: 'dest-in' }])
  .png()
  .toBuffer();

// Accent ring behind portrait
const ring = Buffer.from(
  `<svg width="${PORTRAIT + 16}" height="${PORTRAIT + 16}"><circle cx="${(PORTRAIT + 16) / 2}" cy="${(PORTRAIT + 16) / 2}" r="${(PORTRAIT + 14) / 2}" fill="none" stroke="${accentLight}" stroke-width="4" stroke-opacity="0.7"/></svg>`,
);

await sharp(bg)
  .composite([
    { input: ring, left: PORTRAIT_X - 8, top: PORTRAIT_Y - 8 },
    { input: portrait, left: PORTRAIT_X, top: PORTRAIT_Y },
  ])
  .png()
  .toFile(join(root, 'public/assets/og-image.png'));

console.log('✓ Wrote public/assets/og-image.png (1200x630)');
