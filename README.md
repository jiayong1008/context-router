# The Context Router

**Stop explaining your projects to AI over and over.**

Say *"what's the status on Nova"* and your AI finds the right file, loads everything it knows about that project, and answers. No re-pasting context. No re-explaining who's involved.

Four markdown files. Nothing to install.

---

## Is this for me?

Yes, if you keep notes in files and you use AI regularly. You do **not** need to be technical.

- **You don't need Obsidian.** Any folder of notes on your computer works. (Obsidian just makes it nicer to browse.)
- **You don't need a coding tool.** Works with Claude, ChatGPT, or Gemini in a browser — see Path B below.
- **You don't need organized notes yet.** The setup interview helps you sort that out.

---

## Quick start

*Three steps. Nothing to install.*

### Step 1 — Get the files

Green **Code** button at the top of this page → **Download ZIP** → unzip it.

### Step 2 — Put them in your notes folder

Copy all the files into the **top level** of wherever you keep notes.

> **"Top level" means:** the main folder that holds your other note folders — not inside any one of them. If your notes live in `Documents/My Notes/` and inside that you have `Work/`, `Personal/`, `Ideas/` — then `Documents/My Notes/` is the top level. That's where these files go, sitting alongside `Work/` and the rest.
>
> If you use Obsidian, this is your **vault folder** — the one you picked when you first opened Obsidian. Right-click your vault name → *Reveal in Finder / Explorer* if you're not sure where it is.

### Step 3 — Tell your AI to set it up

Say this, exactly:

> Read the START HERE file and set this up with me.

Your AI will ask you questions — what you're working on, who's involved, what you'd actually type when you mean each project — and write your files from your answers.

**About 15 minutes for a couple of projects; nearer half an hour if you have several.** You don't fill in any templates yourself.

---

## Which path applies to you?

Both end in the same place. Pick whichever matches how you use AI.

### Path A — your AI can open your folder

*Claude Code, Codex, Cursor — tools that run on your computer and read your files.*

Open the tool **in your notes folder**, then say the sentence from Step 3. It writes every file for you, in the right place. Done.

Tools differ in whether they pick up a rules file on their own: Claude Code reads `CLAUDE.md` automatically, and several others read `AGENTS.md` — both ship in the kit, so one of them usually lands. If yours does neither, just say *"read CLAUDE.md first"* at the start of a session and everything else works the same.

### Path B — you chat with AI in a browser or app

*Claude, ChatGPT, Gemini — you type in a window and upload files.*

Your AI can't reach your folder, so you hand it the files:

1. Start a new chat — or a **Project**, if your tool has them (Claude Projects, ChatGPT Projects). A Project remembers the files across every future chat instead of just one, which is much better.
2. Upload `01 START HERE`, `CLAUDE.md`, `MEMORY.md`, and `_TEMPLATE_CONTEXT.md`.
3. Say the sentence from Step 3.
4. It interviews you, then hands back finished files with instructions on where to save each one. Copy each into your notes folder as it tells you.

After that, at the start of a conversation, upload or paste `MEMORY.md` plus the one project file you're working on.

> **Being straight about Path B:** your AI can't go and fetch files, so *you* pick which
> project file to hand it. What you get here is a reusable, well-organised context pack
> rather than automatic lookup — you stop re-explaining your projects, but you're still the
> one opening the drawer. Automatic routing needs Path A.
>
> Most people start here anyway, and that's fine. Everything you build still works if you
> later switch to a tool that reads your folder — that's the point of plain markdown.

---

## Did it work?

Open a **brand new** chat or session and ask:

> What's the status on [one of your projects]?

Use only the project's nickname — don't tell it which file to read.

- ✅ **It works** if the AI pulls up that project's details and answers from them.
- ❌ **Needs a tweak** if it says it doesn't know, or starts reading everything. Your trigger words are too narrow — open `CLAUDE.md`, find the routing table, and add the words you actually just used.

**Also worth 30 seconds:** open `MEMORY.md` and `CLAUDE.md` yourself and look at them. The routing table should have one row per project, and `MEMORY.md` should describe you and your work. AI assistants sometimes say they've written a file when they haven't — a quick look is the only way to catch that.

---

## What each file does

| File | What it's for | Do I edit it? |
| :--- | :--- | :--- |
| `01 START HERE` | The interview script your AI follows to set you up | No — just point your AI at it |
| `CLAUDE.md` | The rules + the routing table (project → file) | Your AI fills the table in |
| `AGENTS.md` | Same thing, different filename, so other AI tools find it | No |
| `MEMORY.md` | Short always-loaded index: you, your projects, key people | Your AI fills it in |
| `_TEMPLATE_CONTEXT.md` | The shape each project's file takes | No — it's a blueprint |
| `Projects/_EXAMPLE Nova/` | A filled-in example so you can see what a real one looks like | Delete it once you've looked |
| `check-routing.py` | Finds projects missing from your routing table, and rows pointing at files that are gone | No, just run it |

> **Your own projects don't go in a `Projects/` folder.** They stay wherever they
> already live — `Work/Clients/Nova/`, `Uni/Thesis/`, whatever you already use. Each
> one just gets a `_CONTEXT.md` inside it. The `Projects/` folder here exists only to
> hold the example, and you can delete the whole thing.

---

## Using it day to day

Setup happens once. After that:

**If your AI reads your folder** (Claude Code, Codex, Cursor) — open it in your notes folder and just start talking. It reads the rules and your index on its own. Nothing to paste, nothing to remember.

**If you chat in a browser** — put `CLAUDE.md` and `MEMORY.md` into a Project once, and they're there for every future chat. Add the one `_CONTEXT.md` you're working on when you need depth. If your tool has no Projects feature, paste `MEMORY.md` at the start of a conversation.

Then it's just normal conversation:

- *"What's the status on Nova?"* — it opens Nova's file and answers from it.
- *"Remember that Priya approved the SMS wording."* — it writes that to the right file and tells you which.
- *"I'm starting a new project with a client called Atlas."* — it creates the context file, adds a routing row, and adds a memory line, without being asked.

You never say which file to open. That's the whole point.
---

## How it actually works

Two layers:

**Always loaded** — `MEMORY.md`, a one-screen index of who you are and what's active. Small on purpose.

**Loaded on demand** — one `_CONTEXT.md` per project, holding the real detail. Opened only when that project comes up.

A **routing table** in `CLAUDE.md` connects them: the words you'd actually type → the file to open. So "the Nova thing" opens Nova's file. Your shorthand, your misspellings, all of it goes in the table.

That's why ten projects and forty projects cost the same per conversation. The router just has more rows.

---

## Keeping it alive

Small habits. The system rots without them.

- **Say "remember this"** mid-conversation. Your AI knows which file it belongs in.
- **Let it update the project file** when something changes — deleting what stopped being true in the same pass. Finished items get *removed*, not ticked off.
- **New project = three things**, which your AI does unprompted: a project file, a routing row, a memory line.
- **Once a month, skim the routing table.** Delete dead projects, add anything that never got indexed. Five minutes.

---

## If something goes wrong

| What you're seeing | What's happening | Fix |
| :--- | :--- | :--- |
| AI ignores the files entirely | It can't read your folder, or you opened it somewhere else | Use Path B, or reopen your tool inside your notes folder |
| It reads everything anyway | Nothing in the routing table matched what you typed | Add the words you actually used to the table in `CLAUDE.md` |
| Answers are out of date | Old lines never got deleted | Check for finished items ticked off instead of removed — delete them |
| Sessions feel slow again | `MEMORY.md` grew too big | It should fit on one screen. Move long entries into the project's own file |
| A project vanished from the routing table | Normal drift — it got created mid-conversation and never indexed | That's what the monthly skim is for |

---

## Catching drift

The routing table is maintained by hand, so it goes stale. Projects get created mid-conversation and never indexed; projects end and their rows linger. Both are quiet failures: the AI simply never finds a file, and you assume it looked.

There's a script for that:

```
python3 check-routing.py /path/to/your/notes
```

No dependencies, nothing installed. It reports two things:

- **Not routed** — a project has a `_CONTEXT.md` but nothing in the table points at it. Your AI will never find it on its own.
- **Dead rows** — the table points at a file that isn't there any more. The project moved, or ended.

Run it monthly, or whenever answers start feeling stale. It exits 0 when clean, so you can wire it into whatever you already run.

It finds the routing table even if you keep a thin `CLAUDE.md` at the root and the real table one folder down, and it ignores the example rows in this kit's own templates.

## Honest limits

- **This is keyword matching, not search.** No AI magic underneath — just a table you maintain. Fine for a personal vault, a real ceiling past a few dozen projects.
- **It's maintained by hand.** Nothing enforces the routing table. It's accurate because you keep it accurate.
- **It's a habit, encoded as files.** If you wouldn't keep a project's notes current, this will rot for the same reason. The pattern doesn't create the discipline — it makes the discipline pay off.

---

*Built by Lim Jia Yong — software engineering lead, Malaysia. I build practical AI and automation systems, and this is the setup I actually run.*

*[@JiaYongLim1008 on X](https://x.com/JiaYongLim1008) · [GitHub](https://github.com/jiayong1008) · [LinkedIn](https://www.linkedin.com/in/lim-jia-yong/)*

*Copy it, fork it, change it. No permission needed.*
