<a name="readme-top"></a>
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]

<!-- PROJECT LOGO -->
<div align="center">
  <h3 align="center">geckolib-animation-converter</h3>
  <p align="center">
    A simple Python script to convert <a href="https://github.com/bernie-g/geckolib">GeckoLib</a> animations exported from Blockbench as Bedrock .animation.json files into Java Edition compatible files.
    <br />
    🐛 <a href="https://github.com/ssyyhhrr/geckolib-animation-converter/issues">Report Bug</a>
    ·
    ✨ <a href="https://github.com/ssyyhhrr/geckolib-animation-converter/issues">Request Feature</a>
  </p>
</div>

---

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#-about-the-project">About The Project</a></li>
    <li><a href="#-usage">Usage</a></li>
    <li><a href="#-contributing">Contributing</a></li>
    <li><a href="#-license">License</a></li>
    <li><a href="#-contact">Contact</a></li>
  </ol>
</details>

---

<!-- ABOUT THE PROJECT -->

## 🔗 About The Project

Blockbench's Bedrock animation export writes some keyframes as objects with `pre` and `post`
values (for smooth interpolation, or a jump at a keyframe). The Java Edition version of GeckoLib
expects a plain value at each keyframe, so it can't read them. This script replaces every such
keyframe with its `post` value and leaves everything else as it was.

Before:

```json
"rotation": {
  "0.0": [0, 0, 0],
  "0.5": { "post": [0, 45, 0], "lerp_mode": "catmullrom" },
  "1.0": { "pre": [0, 90, 0], "post": [0, 0, 0] }
}
```

After:

```json
"rotation": {
  "0.0": [0, 0, 0],
  "0.5": [0, 45, 0],
  "1.0": [0, 0, 0]
}
```

---

<!-- USAGE -->

## 🚀 Usage

You need Python 3. There's nothing to install.

```sh
python main.py ./model.animation.json ./output.animation.json
```

On Windows, use `py` instead of `python`. The first argument is the exported animation, the
second is where to write the converted one. Give it a new file each time: the script appends
to the output file, so writing over an existing one leaves invalid JSON.

---

<!-- CONTRIBUTING -->

## 🤝 Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull
request. You can also simply open an issue with the tag "enhancement".

Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

<!-- LICENSE -->

## 📄 License

Distributed under the MIT License. See `LICENSE.txt` for more information.

---

<!-- CONTACT -->

## 📬 Contact

Rhys Bishop - [https://sy.hr/](https://sy.hr/) - mail@rhysbi.shop

Project Link: [https://github.com/ssyyhhrr/geckolib-animation-converter](https://github.com/ssyyhhrr/geckolib-animation-converter)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->

[contributors-shield]: https://img.shields.io/github/contributors/ssyyhhrr/geckolib-animation-converter.svg?style=for-the-badge
[contributors-url]: https://github.com/ssyyhhrr/geckolib-animation-converter/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/ssyyhhrr/geckolib-animation-converter.svg?style=for-the-badge
[forks-url]: https://github.com/ssyyhhrr/geckolib-animation-converter/network/members
[stars-shield]: https://img.shields.io/github/stars/ssyyhhrr/geckolib-animation-converter.svg?style=for-the-badge
[stars-url]: https://github.com/ssyyhhrr/geckolib-animation-converter/stargazers
[issues-shield]: https://img.shields.io/github/issues/ssyyhhrr/geckolib-animation-converter.svg?style=for-the-badge
[issues-url]: https://github.com/ssyyhhrr/geckolib-animation-converter/issues
[license-shield]: https://img.shields.io/github/license/ssyyhhrr/geckolib-animation-converter.svg?style=for-the-badge
[license-url]: https://github.com/ssyyhhrr/geckolib-animation-converter/blob/main/LICENSE.txt
