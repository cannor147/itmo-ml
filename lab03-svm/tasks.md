### Лабораторная работа №3. Метод опорных векторов

Реализуйте несколько ядер для метода опорных векторов. Для каждого набора данных и ядра найдите лучшие параметры ядра используя перекрёстную проверку. После нахождения оптимальных параметров для каждого набора данных и ядра нарисуйте, как ваш классификатор классифицирует всё пространство.

#### Набор данных

Используйте наборы данных [chips.csv](https://drive.google.com/file/d/16H80w7VbXHZCTZwn4xmiRVJAdKdsPj6u/) и [geyser.csv](https://drive.google.com/file/d/1zjwbJhHzylpJztTBlISWTHn9CLRkLgZ4/) для тестирования вашего классификатора.

#### Пример

| ![img](https://lh5.googleusercontent.com/Vis2tFsC4HY1rHrf2IiWbaKY4haAVyQC9j-e2XkT7MLZnrvuzq5KNfQ_-BSiVDQZXuRX3pHyx-uiYfCI68rzQo3pQ-XhDRS0qteo77piNKpSAyT6h6N-_UJNcFm9F9bvhWqQCThr) | ![img](https://lh3.googleusercontent.com/KBlty_iJDaWARuWwMz2KLqyvrdp11AW2kDh2MIlMbzCwPW8MWr6kmh0S-bvXrP4eX2FSFPDKvFXmoD9nZzdZoklqrro9cVXWiyYZV2JCdJGTlje32s4xwgRsRf4v3L9f2lwbEaUk) | ![img](https://lh4.googleusercontent.com/VB21P7Q6g-f-Qy213y6odqmKNQJyNHOEic16XSqDMCfKxS0fNhi5Z6iSf-Hr0LXHEisieMfjQ_u_QQTeCOg9ZnZY-M0PhAfN24HE2e8C7Edfct9GtfHoWqePaZmAnjKR6U3pWfv7) |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Linear                                                       | Polynomial                                                   | Gaussian                                                     |

Не обязательно использовать цвета, можно изобразить контуры разделяющей поверхности, главное чтобы было видно её форму и различимы реальные классы объектов.