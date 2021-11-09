import pyglet


def main():
    file = pyglet.resource.media('media/wet-431.mp3')
    file.play()

    pyglet.app.run()


if __name__ == "__main__":
    main()
