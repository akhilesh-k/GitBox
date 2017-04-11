with open('header.md') as f:
    readme = f.read()
with open('CONTRIBUTORS.md') as f:
    readme += f.read()
with open('footer.md') as f:
    readme += f.read()


with open('README.md', 'w') as f:
    f.write(readme)
Contact GitHub API Training Shop Blog About
