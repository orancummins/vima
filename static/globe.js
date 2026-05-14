export default function MastercardGlobeDemo() {
  const services = [
    "Fraud Detection",
    "Cross-Border Payments",
    "Tokenization",
    "Identity Services",
    "Cybersecurity",
    "Open Banking",
    "Loyalty Programs",
    "Commercial Payments",
    "Digital Wallets",
    "Real-Time Payments",
    "AI Decisioning",
    "Merchant Analytics",
  ];

  return (
    <div className="min-h-screen bg-black flex items-center justify-center overflow-hidden p-10">
      <MastercardGlobe
        services={services}
        globeSize={520}
        rotationSpeed={0.0035}
        glowIntensity={0.8}
      />
    </div>
  );
}

import React, { useEffect, useMemo, useRef, useState } from "react";
import { motion } from "framer-motion";

function MastercardGlobe({
  services = [],
  globeSize = 500,
  rotationSpeed = 0.003,
  glowIntensity = 1,
}) {
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  const [rotation, setRotation] = useState(0);

  const points = useMemo(() => {
    const generated = [];
    const total = Math.max(services.length, 60);

    for (let i = 0; i < total; i++) {
      const phi = Math.acos(-1 + (2 * i) / total);
      const theta = Math.sqrt(total * Math.PI) * phi;

      const x = Math.cos(theta) * Math.sin(phi);
      const y = Math.sin(theta) * Math.sin(phi);
      const z = Math.cos(phi);

      generated.push({
        x,
        y,
        z,
        label: services[i % services.length] || `Service ${i + 1}`,
      });
    }

    return generated;
  }, [services]);

  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    const render = () => {
      ctx.clearRect(0, 0, globeSize, globeSize);

      const radius = globeSize * 0.32;
      const centerX = globeSize / 2;
      const centerY = globeSize / 2;

      const gradient = ctx.createRadialGradient(
        centerX,
        centerY,
        radius * 0.2,
        centerX,
        centerY,
        radius
      );

      gradient.addColorStop(0, "rgba(255,140,0,0.18)");
      gradient.addColorStop(0.45, "rgba(255,94,0,0.10)");
      gradient.addColorStop(1, "rgba(0,0,0,0)");

      ctx.fillStyle = gradient;
      ctx.beginPath();
      ctx.arc(centerX, centerY, radius * 1.35, 0, Math.PI * 2);
      ctx.fill();

      ctx.strokeStyle = `rgba(255,120,0,${0.15 * glowIntensity})`;
      ctx.lineWidth = 1;

      for (let lat = -80; lat <= 80; lat += 20) {
        ctx.beginPath();

        for (let lon = 0; lon <= 360; lon += 5) {
          const latRad = (lat * Math.PI) / 180;
          const lonRad = ((lon * Math.PI) / 180) + rotation;

          const x = Math.cos(latRad) * Math.cos(lonRad);
          const y = Math.sin(latRad);
          const z = Math.cos(latRad) * Math.sin(lonRad);

          const scale = 1 / (1.8 - z);

          const px = centerX + x * radius * scale;
          const py = centerY + y * radius * scale;

          if (lon === 0) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }

        ctx.stroke();
      }

      for (let lon = 0; lon < 360; lon += 20) {
        ctx.beginPath();

        for (let lat = -90; lat <= 90; lat += 5) {
          const latRad = (lat * Math.PI) / 180;
          const lonRad = ((lon * Math.PI) / 180) + rotation;

          const x = Math.cos(latRad) * Math.cos(lonRad);
          const y = Math.sin(latRad);
          const z = Math.cos(latRad) * Math.sin(lonRad);

          const scale = 1 / (1.8 - z);

          const px = centerX + x * radius * scale;
          const py = centerY + y * radius * scale;

          if (lat === -90) ctx.moveTo(px, py);
          else ctx.lineTo(px, py);
        }

        ctx.stroke();
      }

      points
        .sort((a, b) => b.z - a.z)
        .forEach((point) => {
          const rotatedX =
            point.x * Math.cos(rotation) - point.z * Math.sin(rotation);

          const rotatedZ =
            point.x * Math.sin(rotation) + point.z * Math.cos(rotation);

          const scale = 1 / (1.8 - rotatedZ);

          const px = centerX + rotatedX * radius * scale;
          const py = centerY + point.y * radius * scale;

          const opacity = Math.max(0.15, scale - 0.2);
          const visible = rotatedZ > -0.15;

          if (!visible) return;

          ctx.beginPath();
          ctx.fillStyle = `rgba(255,140,0,${opacity})`;
          ctx.shadowColor = "rgba(255,120,0,0.9)";
          ctx.shadowBlur = 10;
          ctx.arc(px, py, 2.5 * scale, 0, Math.PI * 2);
          ctx.fill();

          ctx.font = `${Math.max(10, 12 * scale)}px sans-serif`;
          ctx.fillStyle = `rgba(255,255,255,${opacity})`;
          ctx.fillText(point.label, px + 10, py + 4);
        });

      setRotation((prev) => prev + rotationSpeed);
      animationRef.current = requestAnimationFrame(render);
    };

    render();

    return () => cancelAnimationFrame(animationRef.current);
  }, [points, globeSize, rotation, rotationSpeed, glowIntensity]);

  return (
    <motion.div
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 1.2 }}
      className="relative"
    >
      <div
        className="absolute inset-0 rounded-full blur-3xl opacity-50"
        style={{
          background:
            "radial-gradient(circle, rgba(255,98,0,0.35) 0%, rgba(255,98,0,0) 70%)",
        }}
      />

      <canvas
        ref={canvasRef}
        width={globeSize}
        height={globeSize}
        className="relative z-10"
      />

      <div className="absolute inset-0 rounded-full border border-orange-500/20" />

      <div className="absolute bottom-10 left-1/2 -translate-x-1/2 text-center z-20">
        <div className="text-orange-400 text-sm tracking-[0.35em] uppercase mb-2">
          Mastercard Global Services
        </div>
        <div className="text-white/60 text-xs max-w-sm">
          Dynamic rotating visualization of globally available Mastercard
          capabilities.
        </div>
      </div>
    </motion.div>
  );
}
