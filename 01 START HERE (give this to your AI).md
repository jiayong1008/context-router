# START HERE — Setup Interview

**You are an AI agent. Someone just gave you this file. Your job is to interview them and build their Context Router.**

Do not skip the interview. Do not fill these files in with guesses. The whole system only works if the content is true, and only the human knows what's true.

**First, work out which situation you're in — it changes how you finish:**

- **You can read and write files in their vault** (you're an agent CLI with folder access). Write each file yourself, in place, as you go. Tell them the path each time.
- **You can't touch their files** (you're a chat window and they uploaded this). Same interview, but at the end of each round, output the finished file as a code block and tell them exactly where to save it — filename and folder. Don't assume they know markdown; say "create a file called `MEMORY.md` in your main notes folder and paste this in."

If you're unsure which, ask them: *"Can you see my files directly, or should I give you the finished files to save yourself?"*

---

## What you are building

Four files at the vault root that let any AI agent navigate this person's notes without reading everything:

| File | Role |
| :--- | :--- |
| `CLAUDE.md` | Rules + the routing table. Read first, every session. |
| `AGENTS.md` | A pointer to CLAUDE.md, for tools that look for this name instead. |
| `MEMORY.md` | Lean always-loaded index: who they are, what's active, who matters. |
| `[Project]/_CONTEXT.md` | Deep detail for one project. Loaded only when relevant. |

`CLAUDE.md` and `AGENTS.md` are already written and need no changes. Your job is `MEMORY.md`, the routing table inside `CLAUDE.md`, and one `_CONTEXT.md` per active project.

---

## How to run the interview

**Rules:**

- Ask in small batches — three to five questions at a time, never a wall of them.
- Ask follow-ups when an answer is vague. "Client work" is not enough; you need the client's name and what you'd actually type when you mean them.
- Never invent a fact. If something stays unclear, write `unknown — ask me` in the file. That is a feature: it tells the agent to ask instead of guessing later.
- Keep it under fifteen minutes. You can always add projects later.
- Write the files as you go, at the end of each round. Don't hold everything to the end.

---

### Round 1 — Who they are

Ask:

1. What should I call you?
2. In one line each — what are the hats you wear? (job, company, side projects, studies)
3. Where are you based, and is there a timezone or working rhythm I should know?
4. When I answer you, what do you want more of and less of? (e.g. shorter answers, one recommendation instead of options, more pushback)

Write these into the `## Me` section of `MEMORY.md`.

---

### Round 2 — What's active

Ask:

1. What are you actively working on right now? List them — don't filter yet.
2. For each one: what is it, in a sentence someone outside would understand?
3. For each one: what are *you* responsible for there?
4. Anything on that list that's actually finished or dormant? (Drop those — archived work doesn't need routing.)

Aim for three to six projects. If they name more than eight, ask which ones they touched in the last two weeks and start with those.

Write one row per project into the `## Active projects` table in `MEMORY.md`.

---

### Round 3 — Trigger words (the important one)

For each project, ask:

> When you mention this in a rush, what words do you actually use? Include the short name, client or company names, teammate names, product names — anything you'd type instead of the full project name.

Push for real ones. If someone calls it "the Nova thing" or types "ekids" instead of "Edukids", those go in. Misspellings they make often go in too.

**This table is the whole mechanism.** A project with weak trigger words is invisible to the router.

Write these into the `## Routing map` table in `CLAUDE.md`.

---

### Round 4 — Depth, one project at a time

Now create `_CONTEXT.md` for each project. Use `_TEMPLATE_CONTEXT.md` as the shape. For each, ask:

1. Who else is involved, and what do they do?
2. Where does this stand today?
3. What's open — what actually needs doing next?
4. What are you unsure about, or waiting on someone for?

Put the project's file at `[wherever that project's folder lives]/_CONTEXT.md`. If the project has no folder yet, ask where they want it, or create one.

Anything they can't answer becomes a line under `## What I Don't Know Yet`.

---

### Round 5 — People and routines

Ask:

1. Who comes up often across your work? (name + one line on who they are)
2. Any recurring commitments I should know about? (standups, weekly reviews, where daily notes live)

Write these into `## Key people` and `## Routines` in `MEMORY.md`.

---

## When you're done

1. Show them the finished `MEMORY.md` and the routing table, and ask what's wrong. There will be something.
2. Make sure every file has actually landed somewhere — either you wrote it, or they saved it. Confirm the paths out loud.
3. Tell them to test it cold: open a brand-new session and ask *"what's the status on [project]?"* using only a trigger word. If the right context comes up and the answer is drawn from it, it works. If not, the trigger words need more entries.
4. Tell them they can delete this file, or keep it for adding projects later.

---

## After setup — the rules that keep it alive

Remind them of these once, then follow them yourself in every future session:

- **Say "remember this" mid-conversation.** You decide which file it belongs in, using the routing rules in `CLAUDE.md`.
- **Update the project's `_CONTEXT.md`** whenever something meaningful changes — and delete what stopped being true in the same pass.
- **New project = three things, done without asking:** its `_CONTEXT.md`, a routing row, a `MEMORY.md` line.
- **Once a month, skim the routing table.** Remove dead projects. Add anything created live that never got indexed. This drift is normal and this is the fix.

---

*Context Router — a pattern by Lim Jia Yong. Copy it, fork it, change it. No permission needed.*
*[@JiaYongLim1008](https://x.com/JiaYongLim1008)*
